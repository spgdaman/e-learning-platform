from django import forms
from .models import Profile,Course,Assignment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'mobile_no',)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_description',)

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('name', 'link',)