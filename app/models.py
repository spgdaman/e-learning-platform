from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/')
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)

    # Relationships and Foreign Keys
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return self.username

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    course_description = models.CharField(max_length=150)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['course_name']

class Assignment(models.Model):
    name = models.CharField(max_length=40)
    assignment = models.FileField(upload_to='assignments/')
    link = models.URLField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    # Relationships and Foreign Keys
    course = models.ManyToManyField('Course')
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['submitted_at']