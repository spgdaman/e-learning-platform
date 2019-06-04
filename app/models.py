from django.db import models

class Profile(models.Model):
    # profile_pic = models.ImageField()
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)

    # Relationships and Foreign Keys

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    course_description = models.CharField(max_length=150)

    # Relationships and Foreign Keys
    assignment_id=models.ManyToManyField('Assignment')

class Assignment(models.Model):
    name = models.CharField(max_length=40)
    # assignment = models.ImageField()
    link = models.URLField()
