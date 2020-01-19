from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_item, name='add_item'),
    path('all', views.all_items, name='all_items'),
    path('added', views.added, name='added')
]
