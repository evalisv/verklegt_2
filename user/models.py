from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    kennitala = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    municipiality = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    offers = models.TextField(blank=True)
    user_roles = models.TextField()
    messages = models.TextField(blank=True)
    watchlist = models.TextField(blank=True)
    estates = models.TextField(blank=True)