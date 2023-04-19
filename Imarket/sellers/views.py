from django.shortcuts import render

<<<<<<< HEAD
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Seller
from .serializers import SellerSerializer
from .permissions import IsSellerOrReadOnly


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsSellerOrReadOnly,)
=======
# Create your views here.
>>>>>>> f75d9273045ce67d07b6d7eb5b12529bfc1782ac
