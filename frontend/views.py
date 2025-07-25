from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, StudySession
from .forms import NewTask, NewStudySession, RegisterForm
from datetime import timedelta # for study session times

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def tasks(request):
    user = request.user
    form = NewTask()
    study_form = NewStudySession(request.POST)
    tasks = Task.objects.filter(author=user)
    study_sessions = StudySession.objects.filter(author=user)
    if study_form.is_valid():
        study_session = study_form.save(commit=False)
        study_session.author = user
        study_session.save()
        return redirect('tasks')
    else:
        study_form = NewStudySession()
    return render(request, 'tasks.html', context={'form': form, 'tasks': tasks, 'study_sessions': study_sessions, 'study_form': study_form})

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

def create_study_session(request):
    user = request.user
    study_form = NewStudySession(request.POST)
    if study_form.is_valid():
        study_session = study_form.save(commit=False)
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
def leaderboard(request):
    return render(request, 'leaderboard.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def register(request):
    # Initially get the form to display for the user
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    # After user submits form, save the user and display a message
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up for Ekklesia successfully.")
        else:
            messages.error(request,"There was an error when signing up, please check the fields.",)
        return render(request, "registration/register.html", {"form": form})
    
def forgot_password(request):
    return render(request, 'registration/forgot_password.html')