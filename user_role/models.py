from django.db import models
from user.models import User


class UserRole(models.Model):
    role = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
