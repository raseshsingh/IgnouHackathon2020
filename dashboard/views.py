from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import VegetableForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/main-content.html')


@login_required
def add_item(request):
    if request.method == 'POST':
        form = VegetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VegetableForm()
    return render(request, 'dashboard/add-item.html', {'form': form})


@login_required
def all_items(request):
    return render(request, 'dashboard/all_items.html')


@login_required
def added(request):
    return render(request,'dashboard/added.html')