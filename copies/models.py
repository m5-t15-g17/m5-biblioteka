from django.db import models

class Copy(models.Model):
    # class Meta:
    #     ordering = ["id"]
    copyNumber = models.IntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="copy")
    