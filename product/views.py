
from django.db import connection
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product import models, serializers


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing all categories
    """
    
    queryset = models.Category.objects.all()

    @extend_schema(responses=serializers.CategorySerializer)
    def list(self, request):
        serializer = serializers.CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing all brands
    """
    
    queryset = models.Brand.objects.all()

    @extend_schema(responses=serializers.BrandSerializer)
    def list(self, request):
        serializer = serializers.BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class ProductViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing all products
    """
    
    queryset = models.Product.objects.all().is_active()
    # lookup_field = 'name'
    
    def retrieve(self, request, pk=None):
        """
        An endpoint return individual product by id
        """
        serializer = serializers.ProductSerializer(self.queryset.get(pk=pk))
        return Response(serializer.data)
       
            

    @extend_schema(responses=serializers.ProductSerializer)
    def list(self, request):
        serializer = serializers.ProductSerializer(self.queryset.select_related('category', 'brand'), many=True)
        response = Response(serializer.data)
        print(len(connection.queries))
        return response
    
    @action(methods=['GET'], detail=False, url_path=r"category/(?P<category>\w+)/all",)
    def list_of_product_by_category(self, request, category=None):
        """
        An endpoint to return products by category
        """
        serializer = serializers.ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)



class ProductLineViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing all product line
    """
    
    queryset = models.ProductLine.objects.all()

    @extend_schema(responses=serializers.ProductLineSerializer)
    def list(self, request):
        serializer = serializers.ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)


