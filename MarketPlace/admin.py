from django.contrib import admin
# Register your models here.
from .models import HarvestType, Crops, SellHarvestedCrops
# Register your models here.
admin.site.register(HarvestType)
admin.site.register(Crops)
admin.site.register(SellHarvestedCrops)
