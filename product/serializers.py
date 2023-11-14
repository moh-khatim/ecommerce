from rest_framework import serializers

from product import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = models.Product
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = models.ProductLine
        fields = "__all__"