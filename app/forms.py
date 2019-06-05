from django import forms
from .models import Profile,Course,Assignment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['assignment', 'user']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = []

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['submitted_at',]