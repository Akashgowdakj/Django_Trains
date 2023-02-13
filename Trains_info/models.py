from django.db import models

# Create your models here.
class train_details(models.Model):
    train_ID = models.PositiveIntegerField(primary_key=True)
    train_Name = models.CharField(max_length=260, unique =True)
    origin_info = models.CharField(max_length=200)
    destination_info = models.CharField(max_length=200)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

