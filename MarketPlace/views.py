from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import SaleForm
from django.views.generic import ListView
from .models import  Product


class BuyCropProceeds(ListView):
    """
    Generic class-based view listing type of crops for assisting in buying current WholeSaler.
    """
    model = Product
    template_name = 'CropListings.html'


@login_required
def sell_crop(request):
    """
    View function for choosing specific type of crops such as sugarcane,tea
    and then accepting details regarding sale.
    finally this function redirects to market page where farmers can see sale live.
    """
    sold = False
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.save()
            sold = True
    else:
        form = SaleForm()
    return render(request, 'sell_crops.ht'
                           ''
                           'ml', {'form': form, 'sold': sold})
