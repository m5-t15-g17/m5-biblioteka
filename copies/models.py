from django.db import models

class Copie(models.Model):
    # class Meta:
    #     ordering = ["id"]
    quantity = models.IntegerField()