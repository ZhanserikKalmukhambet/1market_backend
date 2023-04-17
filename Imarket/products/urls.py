from django.urls import path
from . import views

from .views import ProductImageViewSet, CategoryViewSet

from rest_framework import routers

urlpatterns = [
    path('products/', views.ProductAPIView.as_view(), name='get product list and creating new product'),
    path('products/<int:pk>/', views.ProductAPIUpdate.as_view(), name='get product details'),
    path('products/delete/<int:pk>/', views.ProductAPIDesrtoy.as_view(), name='delete product'),
]

r = routers.DefaultRouter()

r.register(r'product_images', ProductImageViewSet)
r.register(r'categories', CategoryViewSet)

urlpatterns += r.urls
