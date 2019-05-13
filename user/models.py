from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    country = models.CharField(max_length=255)
    def __str__(self):
        return self.country

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to="media/users", max_length=9999)
    kennitala = models.BigIntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    postal_code = models.ForeignKey('estate.Municipality', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey('estate.Estate', on_delete=models.CASCADE)


