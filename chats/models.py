from django.db import models
from datetime import datetime

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Room(models.Model):
    Roomname = models.CharField(max_length=255,blank=False)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)