from django.core.serializers import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer


class ProductApiView(APIView):
    def get(self, request):
        tasks = Product.objects.all().values()
        return Response({'products': ProductSerializer(tasks, many=True).data})
