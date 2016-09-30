from django.shortcuts import render
from .models import Client

# Create your views here.

def index(request):
    all_client=Client.objects.all()
    context={'all_client':all_client}

    return render(request,'client/client.html',context)