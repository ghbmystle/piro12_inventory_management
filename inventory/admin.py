from django.contrib import admin

from inventory.models import Product, Client

admin.site.register(Product)
admin.site.register(Client)