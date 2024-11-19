from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class user(AbstractUser):
    
    role_choices = (
        ('admin', 'Admin'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=role_choices)