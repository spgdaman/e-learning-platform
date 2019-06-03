from django.shortcuts import render

def intro(request):
    return render(request,'intro.html')

def index(request):
    return render(request,'index.html')