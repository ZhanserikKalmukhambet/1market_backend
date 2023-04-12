from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductApiView.as_view(), name='getting product list')
]