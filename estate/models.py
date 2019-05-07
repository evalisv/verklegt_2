from django.db import models
from user.models import User


class Estate(models.Model):
    address = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    size = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.IntegerField()
    fasteignamat = models.IntegerField()
    brunabotamat = models.IntegerField()
    type = models.CharField(max_length=255)
    year_built = models.IntegerField()
    entry = models.BooleanField()
    garage = models.BooleanField()
    description = models.CharField(max_length=999)
    open_house = models.DateTimeField(null=True, blank=True)
    estate_seller = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField()
    elevator = models.BooleanField()
    date_listed = models.DateTimeField()
    def __str__(self):
        return self.address

class EstateImage(models.Model):
    image = models.CharField(max_length=999)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    def __str__(self):
        return self.image