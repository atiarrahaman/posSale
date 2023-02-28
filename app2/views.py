from django.shortcuts import render
from .models import Product
# Create your views here.


def Home(request):
    return render(request,'dashboard.html')

def ProductInput(request):
    return render(request,'productinput.html')


def ProductList(request):
   
    return render(request,'productlist.html')


def Pos(request):
    return render(request,'pos.html')


def Sale(request):
    return render(request,'sale.html')