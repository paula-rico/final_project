from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=25, null=True, blank=True)
    profession = models.CharField(max_length=25, null=True, blank=True)

