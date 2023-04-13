from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='get category list and creating new category'),
    path('categories/<int:id>/', views.CategoryDetails.as_view(), name='get category details'),
    path('products/', views.ProductList.as_view(), name='get product list and creating new product'),
    path('products/<int:id>/', views.ProductDetails.as_view(), name='get product details'),
]