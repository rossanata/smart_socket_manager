from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LogInUser(models.Model):
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=15)