from django.contrib import admin
from django.urls import path

from inventory.views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail')
]