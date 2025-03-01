# resources/models.py

from django.db import models
import requests
from urllib.parse import urlparse, parse_qs

class Book(models.Model):
    """
    Represents a recommended book resource.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    description = models.TextField(default="", blank=True)
    link = models.URLField(blank=True, help_text="Link to purchase or info")
    rating = models.PositiveIntegerField(default=3, help_text="1 to 5")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class WikiResource(models.Model):
    """
    Represents a Wikipedia article resource.
    """
    title = models.CharField(max_length=200)
    url = models.URLField(help_text="Wikipedia article URL")
    snippet = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=3, help_text="1 to 5")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_wiki_page_title(self):
        """
        Attempt to parse the Wikipedia article title from self.url,
        e.g. 'https://en.wikipedia.org/wiki/Python_(programming_language)' -> 'Python_(programming_language)'
        """
        parsed = urlparse(self.url)
        if 'wikipedia.org' in parsed.netloc and parsed.path.startswith('/wiki/'):
            return parsed.path.replace('/wiki/', '', 1)
        return None

    def get_wiki_thumbnail_url(self):
        """
        Calls Wikipedia's REST API to get a summary that may include a 'thumbnail' field.
        Returns the thumbnail source URL or None if not found.
        NOTE: This is a proof-of-concept and may be slow or rate-limited in production.
        """
        page_title = self.get_wiki_page_title()
        if not page_title:
            return None

        api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            thumb = data.get('thumbnail')
            if thumb:
                return thumb.get('source')
        except:
            return None
        return None


class YouTubeVideo(models.Model):
    """
    Represents a YouTube video resource.
    """
    title = models.CharField(max_length=200)
    channel = models.CharField(max_length=200, blank=True)
    link = models.URLField(help_text="YouTube video link")
    description = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=3, help_text="1 to 5")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_youtube_id(self):
        """
        Attempt to extract the video ID from self.link, handling youtu.be/VIDEO_ID or youtube.com/watch?v=VIDEO_ID
        """
        parsed_url = urlparse(self.link)

        # Case 1: youtu.be/VIDEO_ID
        if 'youtu.be' in parsed_url.netloc:
            return parsed_url.path.lstrip('/')

        # Case 2: youtube.com/watch?v=VIDEO_ID
        if 'youtube.com' in parsed_url.netloc:
            query_dict = parse_qs(parsed_url.query)
            if 'v' in query_dict:
                return query_dict['v'][0]

        return None

    def get_thumbnail_url(self):
        """
        Returns the official YouTube thumbnail URL for the extracted video ID.
        e.g. 'https://img.youtube.com/vi/<VIDEO_ID>/hqdefault.jpg'
        """
        video_id = self.get_youtube_id()
        if video_id:
            return f'https://img.youtube.com/vi/{video_id}/hqdefault.jpg'
        return None
