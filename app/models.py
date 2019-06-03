from django.db import models

class Profile(models.Model):
    # profile_pic = models.ImageField()
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_no = models.IntegerField(max_length=15)

    # Relationships and Foreign Keys
    