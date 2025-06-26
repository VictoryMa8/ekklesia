from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.

# Using ListView to just display a simple list of objects
class Home(ListView):
    template_name = 'home.html'
    queryset = Article.objects.order_by('-created_at')
    context_object_name = "articles"

# DetailView allows us to view a single instance of an object
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'