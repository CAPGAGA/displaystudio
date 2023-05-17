from django.db import models

class FormRequests(models.Model):
    name=models.CharField(max_length=64)
    phone=models.IntegerField(blank=True)
    email=models.EmailField(blank=True)
    date=models.DateField(auto_now_add=True)

    # TODO make field for completion marker

class BotTrustedUsers(models.Model):
    name=models.CharField(max_length=64)
    user_id=models.IntegerField(blank=False, default=0)