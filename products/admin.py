from django.contrib import admin
from .models import Client, Product, Review

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Review)