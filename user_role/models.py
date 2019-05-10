from django.db import models
from django.contrib.auth.models import User


class UserRole(models.Model):
    role = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.role
