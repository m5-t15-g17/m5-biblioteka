from django.db import models


class Loan(models.Model):
    book = models.ForeignKey('books.Book', on_delete = models.PROTECT)
    copy = models.ForeignKey('users.User', on_delete = models.PROTECT)
    user = models.ForeignKey('copies.Copy', on_delete = models.PROTECT)
    return_date = models.DateField()
    loan_date = models.DateField()
    expected_return = models.DateField()
    delay = models.BooleanField()