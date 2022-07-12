from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.make}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})    
