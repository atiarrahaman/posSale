from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login , name='login'),
    path('logout',views.Logout , name='logout'),
    path('error',views.Error , name='error'),
    path('',views.Home , name='home'),
    path('productinput',views.ProductInputs , name='productinput'),
    path('productinputsuccess',views.ProductInputSuccess , name='productinputsuccess'),
    path('productlist',views.ProductList , name='productlist'),
    path('pos',views.Pos , name='pos'),
    path('sale',views.Sale , name='sale'),
    path('delete/<int:id>',views.Delete , name='delete' ),
    path('posdelete/<int:id>',views.PostDelete , name='posdelete' ),
    path('checkout/',views.Checkout , name='checkout' ),
    path('edit/<int:pk>',views.Edit , name='edit' ),
    path('productedit/<int:pk>',views.ProductEdit , name='productedit' ),
    path('expense',views.Expense_data , name='expense' ),
    path('tansaction',views.Tansaction , name='tansaction' ),
    path('cash',views.Cash , name='cash' ),
    path('buyproducts',views.BuyBroducts , name='buyproducts' ),
   
]
