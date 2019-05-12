from django.db import models
from django.contrib.auth.models import User


class Municipality(models.Model):
    postal_code = models.IntegerField(primary_key=True)
    municipality = models.CharField(max_length=255)
    def __str__(self):
        return str(self.postal_code) + " " + str(self.municipality)


class EstateType(models.Model):
    type = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return self.type


class Estate(models.Model):
    address = models.CharField(max_length=255)
    postal_code = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    size = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.IntegerField()
    fasteignamat = models.IntegerField()
    brunabotamat = models.IntegerField()
    type = models.ForeignKey(EstateType, on_delete=models.CASCADE)
    year_built = models.IntegerField()
    entry = models.BooleanField()
    garage = models.BooleanField()
    description = models.CharField(max_length=999)
    open_house = models.DateTimeField(null=True, blank=True)
    estate_seller = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField()
    elevator = models.BooleanField()
    date_listed = models.DateTimeField()
    images = models.FileField(upload_to="media", max_length=9999)
    def __str__(self):
        return self.address


class EstateImage(models.Model):
    image = models.CharField(max_length=999)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class EstatePictures(models.Model):
    url = models.FileField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

