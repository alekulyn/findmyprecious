from django.db import models

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

class Item(models.Model):
    user = models.ForeignKey(User)
    number = models.CharField(max_length=10)

    lost_found = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='images/items/')

class User(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
