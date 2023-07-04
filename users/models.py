from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    user_permissions = models.ManyToManyField(Permission, related_name="user_set_custom")
    groups = models.ManyToManyField(Group, related_name="user_set_custom")
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 127)
    is_auth = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

