from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(db_index=True, max_length=200)
    description = models.TextField(max_length=2000)
    body = models.TextField()
    # Many articles can be from one profile, foreign key
    author = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
     # get_absolute_url tells Django how to generate the URL for the instance
    # reverse() takes a urlpattern (article_detail) and required kwargs (pk) and returns a URL
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})