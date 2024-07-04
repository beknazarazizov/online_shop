from django.contrib import admin
from django.urls import path

from shop.views import index, product_detail, logout, add_comment, add_order

urlpatterns = [
    path('online_shop/', index, name='home'),
    # path('home/',index,name='hom'),
    path('category/<slug:category_slug>/products', index, name='products_of_category'),
    path('product_detail/<slug:slug>',product_detail,name='product_detail'),
    path('product_r/<slug:slug>products',product_detail,name='product_r'),
    path('add_comment/<slug:slug>',add_comment,name='add_comment'),
    path('exspensive/<slug:slug>', product_detail, name='productex'),
    path('add_order/<slug:slug>',add_order,name='add_order'),
    path('logout/',logout,name='logoutx'),

    ]