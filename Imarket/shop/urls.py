from django.urls import path
from rest_framework import routers

from .views import ShopViewSet

urlpatterns = [
]

r = routers.DefaultRouter()

r.register(r'shops', ShopViewSet, basename='shop')

urlpatterns += r.urls
