from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Vegetable(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.FileField(upload_to='vegetables/photos')
    price = models.IntegerField()

    def __str__(self):
        return self.name
