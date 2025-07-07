from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

User = get_user_model() 

class Task(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class StudySession(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    study_time = models.IntegerField() # time is in seconds
    break_time = models.IntegerField() # time is in seconds
    cycles = models.IntegerField(default=0) # number of times break is done