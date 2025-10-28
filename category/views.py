from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer


@extend_schema(tags=['Category'])
class CategoryAPIView(APIView):
    serializer_class = CategorySerializer

    def get(self, request):
        try:
            category = Category.objects.all()
        except Category.DoesNotExist:
            return Response({"error": "Category topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
