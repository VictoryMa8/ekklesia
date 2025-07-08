from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/complete_task/<uuid:uuid>', views.complete_task, name='complete_task'),
    path('tasks/delete_task/<uuid:uuid>', views.delete_task, name='delete_task'),
    path('study_sessions', views.study_sessions, name='study_sessions'),
    path('tasks/delete_study_session/<uuid:uuid>', views.delete_study_session, name='delete_study_session'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
]
