from django.db import models
from datetime import datetime, timedelta


class Loan(models.Model):

    user = models.ForeignKey("users.User", related_name = 'loans', on_delete=models.PROTECT)
    copy = models.ForeignKey("copies.Copy", on_delete=models.PROTECT)
    return_date = models.DateField(default=None)
    loan_date = models.DateField(auto_now_add=True)
    returnDate = models.DateField(default=datetime.now().date() + timedelta(days=7))
    expected_return = models.DateField()

    