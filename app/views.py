from django.shortcuts import render, redirect
from .models import Profile,Course,Assignment
from .forms import ProfileForm,CourseForm,AssignmentForm

def intro(request):
    return render(request,'intro.html')

def index(request):
    assignments = Assignment.objects.all()
    courses = Course.objects.all()
    profiles = Profile.objects.all()
    return render(request,'index.html', {"assignments":assignments,"courses":courses,"profiles":profiles})

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')
    else:
        form = ProfileForm()
    return render(request,'profileupdate.html',{'form':form})

def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    return render(request,'profile.html',{"profile":profile})

def enroll_course(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.profile = current_user
            course.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request,'enrollcourse.html',{'form':form})

def submit_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.save()
            return redirect(index)
    else:
        form = AssignmentForm()
    return render(request,'submitassignment.html',{"form":form})