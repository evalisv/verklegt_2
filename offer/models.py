from django.db import models
from estate.models import Estate
from user.models import User


class Offer(models.Model):
    amount = models.IntegerField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)
    offer_made = models.DateTimeField()
    offer_maker = models.ForeignKey(User, on_delete=models.CASCADE)
    payed = models.BooleanField()
    expires = models.DateTimeField()
