from django.db import models
import datetime
from datetime import timedelta


class Loan(models.Model):
    returnDate = datetime.datetime.now()
    returnDate = returnDate + datetime.timedelta(7,0)

    copy = models.ForeignKey("users.User", on_delete=models.PROTECT)
    user = models.ForeignKey("copies.Copy", on_delete=models.PROTECT)
    return_date = models.DateField(default=None)
    loan_date = models.DateField(auto_now_add=True)
    expected_return = models.DateField(default=returnDate)
    delay = models.BooleanField(default=False)