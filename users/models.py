from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length = 100, unique = True)
    email = models.CharField(max_length = 127)
    is_auth = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)

