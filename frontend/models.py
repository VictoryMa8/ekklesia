from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django_cryptography.fields import encrypt

class Demos(AbstractUser):
    tasks_completed = models.IntegerField(default=0)
    cycles_completed = models.IntegerField(default=0)
    total_time_studied = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='user_images/', null=True, blank=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author = models.ForeignKey(Demos, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    title = encrypt(models.CharField(max_length=100))
    description = encrypt(models.CharField(blank=True, null=True, max_length=1000))

class StudySession(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author = models.ForeignKey(Demos, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = encrypt(models.CharField(max_length=100))
    study_time = models.DurationField() # interval data type in Postgres
    break_time = models.DurationField() # interval data type in Postgres
    cycles = models.IntegerField(default=0) # number of times break is done