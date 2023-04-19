from django.urls import path
from . import views

from .views import ProductImageViewSet, CategoryViewSet, ProductViewSet

from rest_framework import routers

urlpatterns = [
]

r = routers.DefaultRouter()

r.register(r'products', ProductViewSet)
r.register(r'product_images', ProductImageViewSet)
r.register(r'categories', CategoryViewSet)

urlpatterns += r.urls
