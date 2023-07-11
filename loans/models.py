from django.db import models
import datetime
from datetime import timedelta


class Loan(models.Model):
    # returnDate = datetime.datetime.now()
    # returnDate = returnDate + datetime.timedelta(7,0)

    user = models.ForeignKey(
        "users.User", related_name="loans", on_delete=models.PROTECT
    )
    copy = models.ForeignKey("copies.Copy", on_delete=models.PROTECT)
    return_date = models.DateField(default=None, null=True)
    loan_date = models.DateField(auto_now_add=True)
    expected_return = models.DateField()

    # @property
    # def delay(self):
    #     if datetime.now > self.return_date:
    #         return
    #     return False
