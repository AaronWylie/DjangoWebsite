from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

class Destination(models.Model):
    user_name = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=100)
    plant_id = models.IntegerField()
    bot_run = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    location_z = models.IntegerField()
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    bot_number = models.IntegerField()
    accuracy = models.IntegerField()


