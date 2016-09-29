from django.shortcuts import render
from .models import Supplier

# Create your views here.


def index(request):
    all_supplier = Supplier.objects.all()
    context = {'all_supplier': all_supplier}

    return render(request, 'supplier/supplier.html', context)