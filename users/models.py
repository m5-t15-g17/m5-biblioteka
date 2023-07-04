from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    books = models.ManyToManyField('books.Book', related_name = 'user')
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 127)
    is_auth = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

