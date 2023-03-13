from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home , name='home'),
    path('productinput',views.ProductInputs , name='productinput'),
    path('productinputsuccess',views.ProductInputSuccess , name='productinputsuccess'),
    path('productlist',views.ProductList , name='productlist'),
    path('pos',views.Pos , name='pos'),
    path('sale',views.Sale , name='sale'),
    path('delete/<int:id>',views.Delete , name='delete' ),
    path('posdelete/<int:id>',views.PostDelete , name='posdelete' ),
    path('checkout',views.Checkout , name='checkout' ),
    path('edit/<int:pk>',views.Edit , name='edit' ),
    path('productedit/<int:pk>',views.ProductEdit , name='productedit' ),
    
   
]
