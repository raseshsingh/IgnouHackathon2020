from django.urls import path, include
from django.contrib.auth import views
from .views import signup
# from .views import signup

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),

    path('signup', signup, name='signup'),

]
