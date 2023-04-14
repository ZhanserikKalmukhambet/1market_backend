from django.urls import path
from . import views

from rest_framework import routers

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='get category list and creating new category'),
    path('categories/<int:pk>/', views.CategoryDetails.as_view(), name='get category details'),
    path('products/', views.ProductAPIView.as_view(), name='get product list and creating new product'),
    path('products/<int:pk>/', views.ProductAPIUpdate.as_view(), name='get product details'),
    path('products/delete/<int:pk>/', views.ProductAPIDesrtoy.as_view(), name='delete product'),
]

