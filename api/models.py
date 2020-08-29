from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=25, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
