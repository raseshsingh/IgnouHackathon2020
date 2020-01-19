from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FarmerBuyerAccount(models.Model):
    """
    Model for Account creation for farmer or buyer
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.TextField(max_length=500, blank=True)
    Farm_City = models.CharField(max_length=200, blank=True)
    user_types = [
        ('FARMER', 'FARMER'),
        ('BUYER', 'BUYER')]
    user_type = models.CharField(
        max_length=20,
        choices=user_types,
        default='FARMER',
        blank=True
    )

    def __str__(self):
        return self.user


class UserProfile(models.Model):
    """
    Model representing a User Profile by extending User Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=30, blank=True)
    City = models.CharField(max_length=30, blank=True)
    FullAddress = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username
