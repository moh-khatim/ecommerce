from rest_framework import viewsets
from rest_framework.response import Response
from product import models
from product.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    queryset = models.Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
