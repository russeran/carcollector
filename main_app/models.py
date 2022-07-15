
from django.db import models
from django.urls import reverse

# Create your models here.

class Website(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(
        max_length=200,
        help_text="Please enter the full URL to the website.",
        default='https://',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('websites_detail', kwargs={'pk': self.id})    

class Car(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.IntegerField()

    websites = models.ManyToManyField(Website)

    def __str__(self):
        return f"{self.name} - {self.make}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})    


class Comment(models.Model):
    comment = models.TextField(
        max_length=300,
    )
    name = models.CharField(
        max_length=50,
        default="Anonymous"
        )
  
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[:20] + "..."

        

    class Meta:
        ordering = ['-name']
