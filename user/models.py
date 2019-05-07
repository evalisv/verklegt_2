from django.db import models
from django.contrib.auth.models import User as auth_user


class User(models.Model):
    kennitala = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    watchlist = models.TextField(blank=True, null=True)
    auth_user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)


class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
