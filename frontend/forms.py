from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task, StudySession, Demos
from datetime import timedelta

class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'A descriptive title...'}),
            'description': forms.TextInput(attrs={'class': 'input mt-5', 'placeholder': 'A descriptive description...'}),
        }

class NewStudySession(forms.ModelForm):
    study_time_minutes = forms.IntegerField(min_value=5, max_value=600, widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Study time in minutes...', 'value': 25}))
    break_time_minutes = forms.IntegerField(min_value=5, max_value=60, widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Break time in minutes...', 'value': 5}))
    
    class Meta:
        model = StudySession
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'A descriptive title...'}),
        }
    
    # overriding default model form save to convert minutes to DurationField
    def save(self, commit=True):
        study_session = super().save(commit=False) # creates a StudySession without saving it to database
        study_session.study_time = timedelta(minutes=self.cleaned_data['study_time_minutes'])
        study_session.break_time = timedelta(minutes=self.cleaned_data['break_time_minutes'])
        if commit:
            study_session.save()
        return study_session
    
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Applying custom attributes to password fields from UserCreationForm
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter a password...',
            'class': 'input font-sans',
            'label': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat your password...',
            'class': 'input font-sans',
            'label': 'Repeat Password'
        })
    class Meta:
        model = Demos
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter a username...',
                'class': 'input font-sans'
            }),
            'email': forms.EmailInput(attrs={ 
                'placeholder': 'Enter your email...',
                'class': 'input font-sans',
            }),
        }