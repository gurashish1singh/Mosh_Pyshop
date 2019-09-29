from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()    # Will get all products from the database
    context = {
        'products': products
    }
    return render(request,'index.html',context)

# New Product
def new_product(request):
    return HttpResponse('New Product page!')