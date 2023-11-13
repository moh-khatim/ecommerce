from rest_framework import viewsets
from rest_framework.response import Response
from product import models
from drf_spectacular.utils import extend_schema
from product.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple view set for viewing all categories
    """
    
    queryset = models.Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
