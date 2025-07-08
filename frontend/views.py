from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('tasks')
    else:
        form = NewTask()
    return render(request, 'tasks.html', context={'tasks': tasks, 'form': form})

@login_required
def delete_task(request, uuid):
    task = get_object_or_404(Task, uuid=uuid)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return redirect('tasks')

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