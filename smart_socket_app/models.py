from django.contrib.auth.models import User
from django.db import models


class SmartSocket(models.Model):
    name = models.CharField(max_length=25, blank=False)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    unique_address = models.CharField(max_length=35, null=True, blank=True)
