from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'
