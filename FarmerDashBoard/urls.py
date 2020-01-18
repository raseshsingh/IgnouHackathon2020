from django.urls import path
from .views import dashboard

urlpatterns = [
    path('dash', dashboard, name='DashBoard'),

]
