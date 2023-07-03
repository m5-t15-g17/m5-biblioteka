from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    books = models.ManyToManyField('Book', related_name = 'users')
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 127)
    is_auth = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    book_history = models.ManyToManyField('Book', related_name = 'user')
