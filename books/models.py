from django.db import models


class Book(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="books")
    description = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    name = models.CharField(max_length=100, unique=True)
