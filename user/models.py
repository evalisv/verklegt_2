from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to='media/users', max_length=9999, blank=True, null=True)
    kennitala = models.BigIntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    postal_code = models.ForeignKey('estate.Municipality', on_delete=models.CASCADE)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey('estate.Estate', on_delete=models.CASCADE)


