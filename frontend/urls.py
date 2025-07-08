from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('study_sessions', views.study_sessions, name='study_sessions'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
]
