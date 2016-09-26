from django.shortcuts import render
from .models import Medicine

# Create your views here.

def index(request):
    all_med=Medicine.objects.all()
    context={'all_med':all_med}
    return render(request,'medicine/medicine.html',context)