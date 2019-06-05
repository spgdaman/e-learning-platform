from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/')
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)

    # Relationships and Foreign Keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ManyToManyField('Course')

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    course_description = models.CharField(max_length=150)

    # Relationships and Foreign Keys
    assignment=models.ManyToManyField('Assignment')

class Assignment(models.Model):
    name = models.CharField(max_length=40)
    assignment = models.FileField()
    link = models.URLField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    profile = models.ManyToManyField('Profile')