from django.contrib.auth.models import User
from django.db import models

class SearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    query = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)