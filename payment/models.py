from django.db import models
from django.contrib.auth.models import User
from estate.models import Estate
from offer.models import Offer

class Payment(models.Model):
    offer = models.OneToOneField(Offer, null=True, blank=True,on_delete=models.CASCADE)
    received = models.DateTimeField()





