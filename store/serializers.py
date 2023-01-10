from rest_framework import serializers
from .models import Product, ProductCategory
from custom_user.models import Customer


class ProductCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductCategory
        fields = ["id", "category"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ["password", "groups", "user_permissions"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields="__all__"
        read_only_fields = ["category_details"]

    category_details = ProductCategorySerializer(
        read_only=True, many=True, source="productcategory_set"
    )
    owner = CustomerSerializer(read_only=True)