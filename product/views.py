from rest_framework import viewsets
from rest_framework.response import Response
from product import models
from drf_spectacular.utils import extend_schema
from product import serializers


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