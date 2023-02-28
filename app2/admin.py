
from django.contrib import admin
from .models import Product,Suplyer,ProductInput

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','item_name','price','status']

@admin.register(ProductInput)
class ProductInputAdmin(admin.ModelAdmin):
    list_display=['id','item_name','qty','sypplyer_name']


@admin.register(Suplyer)
class SuplyerAdmin(admin.ModelAdmin):
    list_display=['id','sypplyer_name']