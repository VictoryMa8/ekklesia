from django import forms
from .models import Task, StudySession

class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'A title for your task...'}),
            'description': forms.TextInput(attrs={'class': 'input mt-5', 'placeholder': 'A description for your task...'}),
        }