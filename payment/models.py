from django.db import models


class Payment(models.Model):
    amount = models.IntegerField()
    received = models.DateTimeField()
    payment_method = models.CharField(max_length=999)
