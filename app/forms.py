from django.forms import forms
from .models import Profile,Course,Assignment

class ProfileForm(forms.Form):
    class meta:
        model = Profile
        fields = ('username', 'email', 'mobile_no')

class CourseForm(forms.Form):
    class meta:
        model = Course
        fields = ('course_name', 'course_description')

class AssignmentForm(forms.Form):
    class meta:
        model = Assignment
        fields = ('name', 'link')