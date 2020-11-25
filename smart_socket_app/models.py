from django.db import models


class LogInProfile(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=15)
