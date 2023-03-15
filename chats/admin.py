from django.contrib import admin
from .models import Room,Message,UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Room)
admin.site.register(Message)