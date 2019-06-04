from django.shortcuts import render
from .models import Profile,Course,Assignment
from .forms import ProfileForm,CourseForm,AssignmentForm

def intro(request):
    return render(request,'intro.html')

def index(request):
    return render(request,'index.html')

def update_profile(request):
    form = ProfileForm()
    return render(request,'profileupdate.html',{'form':form})