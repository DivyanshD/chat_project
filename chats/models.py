from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=255,blank=False)

    def __str__(self):
        return self.name

# class Rooms(models.Model):
#     room_name = models.CharField(max_length=255 , unique=True)

#     def __str__(self):
#         render = self.room_name

# class messages(models.Model):
#     room
#     messages = models.TextField(max_length=300)
#     datetime = models.DateTimeField(datetime=datetime.now())