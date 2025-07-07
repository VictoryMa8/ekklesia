from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task, StudySession
from .forms import NewTask

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def tasks(request):
    user = request.user
    tasks = Task.objects.filter(author=user)
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = user
            task.save()
            return render(request, 'tasks.html', context={'tasks': tasks, 'form': form})
    else:
        form = NewTask()
    return render(request, 'tasks.html', context={'tasks': tasks, 'form': form})

@login_required
def study_sessions(request):
    return render(request, 'study_sessions.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def contact(request):
    return render(request, 'contact.html')