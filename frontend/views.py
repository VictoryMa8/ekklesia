from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Profile

# @login_required
def index(request):
    return render(request, 'index.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', context={"posts": posts })

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')