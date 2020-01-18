from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'HomePage.html')


def dashboard(request):
    return render(request, 'dashboard/index.html')
