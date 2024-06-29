from django.contrib import admin
from django.urls import path

from shop.views import index,product_detail

urlpatterns = [
    path('online_shop/', index, name='home'),
    path('product_detail',product_detail,name='product_detail'),
    ]