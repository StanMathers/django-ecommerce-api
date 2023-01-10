from rest_framework import serializers
from .models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductCategory
        fields = ["id", "category"]


class ProductSerializer(serializers.ModelSerializer):
    category_details = ProductCategorySerializer(
        read_only=True, many=True, source="productcategory_set"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "unit_price",
            "discount",
            "stock",
            "category_details",
        ]
        read_only_fields = ["category_details"]
