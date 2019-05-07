from django.db import models
from user.models import User
from estate.models import Estate


class Vhistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    view_date = models.DateTimeField()

    def __str__(self):
        return estate.addess