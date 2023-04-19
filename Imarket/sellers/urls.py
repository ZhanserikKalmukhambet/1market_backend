from django.urls import path
from rest_framework import routers
from .views import SellerViewSet

urlpatterns = []

r = routers.DefaultRouter()
r.register(r'sellers', SellerViewSet)

urlpatterns += r.urls
