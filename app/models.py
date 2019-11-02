from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    class Meta:
        app_label = 'findmyprecious.app'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

class Comment(models.Model):
    class Meta:
        app_label = 'findmyprecious.app'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

