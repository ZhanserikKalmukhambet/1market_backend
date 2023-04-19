from rest_framework import routers

from .views import UserViewSet

urlpatterns = []

r = routers.DefaultRouter()
r.register(r'users', UserViewSet)

urlpatterns += r.urls
