from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class HarvestType(models.Model):
    """
    Model representing a Crop Genre
    """
    CropGenre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.CropGenre


class Crops(models.Model):
    """
    Model representing a specific crop of Genre
    (i.e. Tea is specific type of plantation of crops).
    """
    crop_name = models.CharField(max_length=50)

    def __str__(self):
        return self.crop_name


class SellHarvestedCrops(models.Model):
    """
    Model representing a accepting details from farmers for assisting
    in making sell of harvested crops.
    """
    Quantity = models.IntegerField(default=0, help_text='In tonnes')
    Farm_image = models.ImageField(upload_to='farm_image', blank=True)
    Harvest_Variety = models.CharField(max_length=100, blank=True)
    Harvest_Description = models.CharField(max_length=500, blank=True)
    Harvest_Type = models.ForeignKey(HarvestType, related_name='crops', on_delete='CASCADE')
    Crop_Name = models.ForeignKey(Crops, related_name='sellCrops', on_delete='CASCADE')
    sold_by = models.ForeignKey(User, related_name='farmers', on_delete='CASCADE')

    PREMIUM = 'P'
    VERY_GOOD = 'VG'
    GOOD = 'G'
    JUST_RIGHT = 'JR'
    quality_standards = [
        (PREMIUM, 'PREMIUM'),
        (VERY_GOOD, 'VERY GOOD'),
        (GOOD, 'GOOD'),
        (JUST_RIGHT, 'JUST RIGHT'),
    ]
    quality = models.CharField(
        max_length=2,
        choices=quality_standards,
        default=PREMIUM,
        blank=True,
        help_text='Quality of crop'
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}  {1} sold by {2}'.format(self.quality, self.Crop_Name, self.sold_by)


class Product(models.Model):
    Quantity = [
        ('10 kg', 'PREMIUM'),
        ('20 kg', 'VERY GOOD'),
        ('30 kg', 'GOOD'),
        ('40 kg', 'JUST RIGHT'),
    ]
    Crop_Name = models.CharField(max_length=100, blank=True)
    Image = models.ImageField(upload_to='farm_image', blank=True)
    PREMIUM = 'P'
    VERY_GOOD = 'VG'
    GOOD = 'G'
    JUST_RIGHT = 'JR'
    quality_standards = [
        (PREMIUM, 'PREMIUM'),
        (VERY_GOOD, 'VERY GOOD'),
        (GOOD, 'GOOD'),
        (JUST_RIGHT, 'JUST RIGHT'),
    ]
    quality = models.CharField(
        max_length=2,
        choices=quality_standards,
        default=PREMIUM,
        blank=True,
        help_text='Quality of crop'
    )
    quantity = models.CharField(
        max_length=2,
        choices=Quantity,
        default=PREMIUM,
        blank=True,
        help_text='Quality of crop'
    )
    Crop_Description = models.CharField(max_length=500, blank=True)
