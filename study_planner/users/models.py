# # from django.db import models
# # from django.contrib.auth.models import User
# # from PIL import Image

# # class Profile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
# #     def __str__(self):
# #         return f'{self.user.username} Profile'
    
# #     def save(self, *args, **kwargs):
# #         super().save(*args, **kwargs)
        
# #         img = Image.open(self.image.path)
# #         if img.height > 300 or img.width > 300:
# #             output_size = (300, 300)
# #             img.thumbnail(output_size)
# #             img.save(self.image.path)





# # # users/models.py
# # from django.db import models

# # # No custom model needed for basic login/logout/register
# # from django.db import models
# # from django.contrib.auth.models import User
# # from django.db.models.signals import post_save
# # from django.dispatch import receiver

# # class Profile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     bio = models.TextField(max_length=500, blank=True)
# #     profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    
# #     def __str__(self):
# #         return f"{self.user.username}'s Profile"

# # # Signal to create a profile when a user is created
# # @receiver(post_save, sender=User)
# # def create_user_profile(sender, instance, created, **kwargs):
# #     if created:
# #         Profile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_user_profile(sender, instance, **kwargs):
# #     instance.profile.save()


# # users/models.py

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # add extra fields if you want, e.g.:
#     bio = models.TextField(blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         # Create a profile for new users
#         Profile.objects.create(user=instance)
#     else:
#         # For existing users, ensure the profile is saved if it exists
#         instance.profile.save()

# from django.db.models.signals import post_save
# from django.dispatch import receiver



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()




from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile for new users
        Profile.objects.create(user=instance)
    else:
        # For existing users, ensure the profile is saved if it exists
        try:
            instance.profile.save()
        except Profile.DoesNotExist:
            # Create profile if it doesn't exist (for existing users)
            Profile.objects.create(user=instance)