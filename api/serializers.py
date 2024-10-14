from .models import customers,products
from rest_framework import serializers
from django.contrib.auth.models import Group, User


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = ['first_name', 'last_name', 'email', 'phone_number','address','dob']


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = products
        fields='__all__'

#should return customer_details
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()