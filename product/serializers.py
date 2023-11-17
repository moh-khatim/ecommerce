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



class ProductLineSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = models.ProductLine
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    brand_name = serializers.CharField(source= "brand.name")
    category = CategorySerializer()
    category_name = serializers.CharField(source= "category.name")
    product_line = ProductLineSerializer(many=True)
    class Meta:
        model = models.Product
        # fields = "__all__"
        fields = ('name', 'description', 'is_digital', 'is_active', 'brand_name', 'category_name' ,'brand', 'category', 'product_line',)