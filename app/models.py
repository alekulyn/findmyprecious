from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    found = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    title = models.CharField(max_length=64)
    desc = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='images/items/', blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
