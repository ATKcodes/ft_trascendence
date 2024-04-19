from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)


