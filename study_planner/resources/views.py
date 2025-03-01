# # resources/views.py
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
# from django.db.models import Q

# from .models import Book, WikiResource, YouTubeVideo
# from .forms import BookForm, WikiForm, YouTubeForm

# def books_view(request):
#     # 1) Searching
#     query = request.GET.get('q', '')
#     books_qs = Book.objects.all()
#     if query:
#         books_qs = books_qs.filter(
#             Q(title__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
#         )
    
#     # 2) Pagination (6 per page, for example)
#     paginator = Paginator(books_qs.order_by('-created_at'), 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     # 3) Modal form creation
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('books')
#     else:
#         form = BookForm()

#     context = {
#         'page_obj': page_obj,
#         'form': form,
#         'query': query,
#     }
#     return render(request, 'resources/books.html', context)

# def wikipedia_view(request):
#     query = request.GET.get('q', '')
#     wiki_qs = WikiResource.objects.all()
#     if query:
#         wiki_qs = wiki_qs.filter(
#             Q(title__icontains=query) | Q(snippet__icontains=query)
#         )

#     paginator = Paginator(wiki_qs.order_by('-created_at'), 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     if request.method == 'POST':
#         form = WikiForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('wikipedia')
#     else:
#         form = WikiForm()

#     context = {
#         'page_obj': page_obj,
#         'form': form,
#         'query': query,
#     }
#     return render(request, 'resources/wikipedia.html', context)

# def youtube_view(request):
#     query = request.GET.get('q', '')
#     yt_qs = YouTubeVideo.objects.all()
#     if query:
#         yt_qs = yt_qs.filter(
#             Q(title__icontains=query) | Q(description__icontains=query) | Q(channel__icontains=query)
#         )

#     paginator = Paginator(yt_qs.order_by('-created_at'), 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     if request.method == 'POST':
#         form = YouTubeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('youtube')
#     else:
#         form = YouTubeForm()

#     context = {
#         'page_obj': page_obj,
#         'form': form,
#         'query': query,
#     }
#     return render(request, 'resources/youtube.html', context)





# resources/views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Book, WikiResource, YouTubeVideo
from .forms import BookForm, WikiForm, YouTubeForm

def books_view(request):
    query = request.GET.get('q', '')
    books_qs = Book.objects.all()
    if query:
        books_qs = books_qs.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
        )

    paginator = Paginator(books_qs.order_by('-created_at'), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()

    context = {
        'page_obj': page_obj,
        'form': form,
        'query': query,
    }
    return render(request, 'resources/books.html', context)


def wikipedia_view(request):
    query = request.GET.get('q', '')
    wiki_qs = WikiResource.objects.all()
    if query:
        wiki_qs = wiki_qs.filter(
            Q(title__icontains=query) | Q(snippet__icontains=query)
        )

    paginator = Paginator(wiki_qs.order_by('-created_at'), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = WikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wikipedia')
    else:
        form = WikiForm()

    context = {
        'page_obj': page_obj,
        'form': form,
        'query': query,
    }
    return render(request, 'resources/wikipedia.html', context)


def youtube_view(request):
    query = request.GET.get('q', '')
    yt_qs = YouTubeVideo.objects.all()
    if query:
        yt_qs = yt_qs.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(channel__icontains=query)
        )

    paginator = Paginator(yt_qs.order_by('-created_at'), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('youtube')
    else:
        form = YouTubeForm()

    context = {
        'page_obj': page_obj,
        'form': form,
        'query': query,
    }
    return render(request, 'resources/youtube.html', context)
