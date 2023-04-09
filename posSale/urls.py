
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('atiar/', admin.site.urls),
    path('',include('app2.urls') ),
]
