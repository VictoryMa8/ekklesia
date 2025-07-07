from django import forms
from .models import Task, StudySession

class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']