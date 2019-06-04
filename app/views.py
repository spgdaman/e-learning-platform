from django.shortcuts import render
from .models import Profile,Course,Assignment
from .forms import ProfileForm,CourseForm,AssignmentForm

def intro(request):
    return render(request,'intro.html')

def index(request):
    return render(request,'index.html')

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request,'profileupdate.html',{'form':form})