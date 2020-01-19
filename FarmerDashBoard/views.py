from django.shortcuts import render
from django.contrib.auth.models import User
from Farmer_Buyer_Accounts.models import FarmerBuyerAccount


# Create your views here.
def home_page(request):
    return render(request, 'HomePage.html')


def dashboard(request):
    return render(request, 'dashboard/index.html')
