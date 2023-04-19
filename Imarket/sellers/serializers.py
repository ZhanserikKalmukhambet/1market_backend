from rest_framework import serializers

from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    model = Seller
    fields = '__all__'

