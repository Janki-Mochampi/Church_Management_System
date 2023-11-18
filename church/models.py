from django.db import models
from django.conf import settings
from django.contrib.auth.models import  AbstractUser
import uuid
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    gender = (
       ('Male', 'Male'),
       ('Female', 'Female')
    )

    category = (
       ('Adult', 'Adult'),
       ('Teen', 'Teen'),
       ('Sunday School', 'Sunday School'),
       ('Visitor', 'Visitor')
    )
    gender = models.CharField(max_length=20,choices=gender,blank=True,null=True)
    birth_date = models.DateField(max_length=20, blank=True,null=True)
    category = models.CharField(max_length=20,choices=category,blank=True,null=True)

    def __str__(self):
        return self.username

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null= True, blank= True)
    date = models.DateField(max_length=200, blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
class Donation(models.Model):
    type = (
        ('Tithes','Tithes'),
        ('Other Givings', 'Other Givings')
    )
    amount =models.PositiveIntegerField()
    type = models.CharField(max_length=200, choices=type)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    body = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body

