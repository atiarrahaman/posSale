
from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(ProductInputCart)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','item_name','price','qty','status']

@admin.register(ProductInput)
class ProductInputAdmin(admin.ModelAdmin):
    list_display=['id','item_name','qty','sypplyer_name']


@admin.register(Suplyer)
class SuplyerAdmin(admin.ModelAdmin):
    list_display=['id','sypplyer_name']


@admin.register(PosSale)
class PosSaleAdmin(admin.ModelAdmin):
    list_display=['id','item','qty']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display=['id','client_name','tax_number']


@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display=['id','item','order_date']
