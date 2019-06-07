from django.shortcuts import render, redirect
from .models import Profile,Course,Assignment
from .forms import ProfileForm,CourseForm,AssignmentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import FileResponse,Http404

def intro(request):
    return render(request,'intro.html')

def index(request):
    assignments = Assignment.objects.all().order_by('-submitted_at')
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

def courses(request):
    user = request.user
    current_profile = Profile.objects.filter(id=user.id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.profile = current_profile
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('update_profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def pdf_view(request,id):
    pdf = Assignment.objects.filter(id=id)
    return render(request, 'pdf/pdf_view.html', {"pdf":pdf})