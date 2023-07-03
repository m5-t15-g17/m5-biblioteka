from django.db import models


class Book(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="book_history")
    copy_id = models.ForeignKey("copies.Copy", on_delete=models.CASCADE, related_name="book")
    description = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    name = models.CharField(max_length=100, unique=True)
