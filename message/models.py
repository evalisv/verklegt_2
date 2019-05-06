from django.db import models
from user.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_from")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_to")
    message_sent = models.DateTimeField()
    subject = models.CharField(max_length=255)
    message_body = models.CharField(max_length=999)
    message_seen = models.BooleanField()
