from django.db import models
from django.contrib.auth.models import User
from estate.models import Estate
from offer.models import Offer
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Payment(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    received = models.DateTimeField()
    card_number = models.IntegerField(validators=[MaxLengthValidator(16), MinLengthValidator(16)])
    expiration = models.IntegerField(validators=[MaxLengthValidator(4), MinLengthValidator(4)])
    cvc = models.IntegerField(validators=[MaxLengthValidator(3), MinLengthValidator(3)])
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)




