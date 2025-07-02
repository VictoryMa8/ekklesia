from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    return render(request, 'index.html')

def posts(request):
    return render(request, 'posts.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')