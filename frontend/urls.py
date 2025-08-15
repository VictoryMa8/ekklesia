from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create_task/', views.create_task, name='create_task'),
    path('tasks/complete_task/<uuid:uuid>', views.complete_task, name='complete_task'),
    path('tasks/delete_task/<uuid:uuid>', views.delete_task, name='delete_task'),
    path('tasks/create_study_session/', views.create_study_session, name='create_study_session'),
    path('delete_study_session/<uuid:uuid>', views.delete_study_session, name='delete_study_session'),
    path('update_user/<int:study_time>', views.update_user, name='update_user'),
    path('about/', views.about, name='about'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('profile/', views.profile, name='profile'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('health/', views.health, name='health'),
]
