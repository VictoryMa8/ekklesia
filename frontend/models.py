from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save # Signal used for creating a profile when a user is created
from django.shortcuts import reverse


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically create a profile when a user is created
    Every user should have a corresponding profile
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save a profile whenever the user is saved
    Keeps the profile in sync with any changes to the user
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        # Creates a profile if it doesn't exist
        Profile.objects.create(user=instance)
    
class Post(models.Model):
    title = models.CharField(db_index=True, max_length=200)
    description = models.TextField(max_length=2000)
    body = models.TextField()
    # Many posts can be from one profile, foreign key
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # get_absolute_url tells Django how to generate the URL for the instance
    # reverse() takes a urlpattern (post_details) and required kwargs (pk) and returns a URL
    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.pk})
