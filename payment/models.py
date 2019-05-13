from django.db import models
from django.contrib.auth.models import User
from estate.models import Estate

class Payment(models.Model):
    amount = models.IntegerField()
    received = models.DateTimeField()
    card_number = models.IntegerField()
    expiration = models.IntegerField()
    cvc = models.IntegerField()
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)




