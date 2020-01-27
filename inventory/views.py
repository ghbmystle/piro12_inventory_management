from django.shortcuts import render, redirect
from django.urls import reverse
from inventory.models import Product, Client


def product_list(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'inventory/product_list.html', data)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'product': product
    }
    return render(request, 'inventory/product_detail.html', data)