from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='get product list and creating new product'),
    path('products/<int:id>', views.ProductDetails.as_view(), name='get product details'),
]