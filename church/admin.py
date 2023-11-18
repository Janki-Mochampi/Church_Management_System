from django.contrib import admin
from .models import CustomUser,Event,Donation,Message
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(Donation)
admin.site.register(Message)


