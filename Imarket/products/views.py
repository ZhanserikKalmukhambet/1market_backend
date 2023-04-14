from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from django.http import Http404

from .models import Category, Product, ProductImage
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer


# viewset
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return ProductImage.objects.all()[:2]
        return ProductImage.objects.filter(pk=pk)


# using genericViews for simplicity
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ModelSerializer with APIView
class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ProductAPIDesrtoy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

