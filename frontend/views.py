from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, StudySession
from .forms import NewTask, NewStudySession
from datetime import timedelta # for study session times

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def tasks(request):
    user = request.user
    form = NewTask()
    tasks = Task.objects.filter(author=user)
    return render(request, 'tasks.html', context={'form': form, 'tasks': tasks})

def create_task(request):
    user = request.user
    form = NewTask(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = user
        task.save()
    tasks = Task.objects.filter(author=user)
    return render(request, 'fragments/current_tasks.html', context={'tasks': tasks})

@login_required
def complete_task(request, uuid):
    user = request.user
    user.tasks_completed += 1
    user.save()

    task = get_object_or_404(Task, uuid=uuid)
    task.completed = True
    task.save()
    tasks = Task.objects.filter(author=request.user) # fetch all tasks of user
    return render(request, 'fragments/current_tasks.html', context={'tasks': tasks}) # render all tasks in the fragment

@login_required
def delete_task(request, uuid):
    task = get_object_or_404(Task, uuid=uuid) # get specific task to delete
    task.delete() # delete requested task
    tasks = Task.objects.filter(author=request.user) # fetch all tasks of user
    return render(request, 'fragments/current_tasks.html', context={'tasks': tasks}) # render all tasks in the fragment

@login_required
def study_sessions(request):
    user = request.user
    study_sessions = StudySession.objects.filter(author=user)
    if request.method == "POST":
        form = NewStudySession(request.POST)
        if form.is_valid():
            study_session = form.save(commit=False)
            study_session.author = user
            study_session.save()
            return redirect('study_sessions')
    else:
        form = NewStudySession()
    return render(request, 'study_sessions.html', context={'study_sessions': study_sessions, 'form': form})

def create_study_session(request):
    user = request.user
    form = NewStudySession(request.POST)
    if form.is_valid():
        study_session = form.save(commit=False)
        study_session.author = user
        study_session.save()
    study_sessions = StudySession.objects.filter(author=user)
    return render(request, 'fragments/current_study_sessions.html', context={'study_sessions': study_sessions})

@login_required
def delete_study_session(request, uuid):
    study_session = get_object_or_404(StudySession, uuid=uuid)
    study_session.delete()
    study_sessions = StudySession.objects.filter(author=request.user) # fetch all study sessions
    return render(request, 'fragments/current_study_sessions.html', context={'study_sessions': study_sessions}) # render all study sessions in the fragment

@login_required
def update_user(request, study_time):
    user = request.user
    user.cycles_completed += 1
    user.total_time_studied  += study_time
    user.save()

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def contact(request):
    return render(request, 'contact.html')