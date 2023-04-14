from django.urls import path
from . import views

from rest_framework import routers

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='get category list and creating new category'),
    path('categories/<int:pk>/', views.CategoryDetails.as_view(), name='get category details'),
    path('products/', views.ProductList.as_view(), name='get product list and creating new product'),
    path('products/<int:id>/', views.ProductDetails.as_view(), name='get product details'),
]

r = routers.DefaultRouter()
r.register(r'product_images', views.ProductImageViewSet)

urlpatterns += r.urls
