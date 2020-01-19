from django.urls import path
from .views import sell_crop, BuyCropProceeds

urlpatterns = [

    path('sell', sell_crop, name='sellCrop'),
    path('buy', BuyCropProceeds.as_view(), name='buy')
]
