from django.shortcuts import render
from .models import Destination

# Create your views here.

def plants(request, pk_test):
    dests = Destination.objects.all()
    customer = Destination.objects.filter(user_name=pk_test)
    return render(request, "plants.html", {'dests': dests})