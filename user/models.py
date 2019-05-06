from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    kennitala = models.IntegerField()
    phone_number = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    profile_image = models.CharField(max_length=9999)
