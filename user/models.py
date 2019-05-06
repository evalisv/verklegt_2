from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    kennitala = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    watchlist = models.TextField(blank=True, null=True)


class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
