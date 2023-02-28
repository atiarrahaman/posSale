from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home , name='home'),
    path('productinput',views.ProductInput , name='productinput'),
    path('productlist',views.ProductList , name='productlist'),
    path('pos',views.Pos , name='pos'),
    path('sale',views.Sale , name='sale'),
]
