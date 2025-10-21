from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from waitlist.models import WaitList
from waitlist.serializers import WaitListSerializer


@extend_schema(tags=['WaitList'], request=WaitListSerializer, responses=WaitListSerializer)
class WaitListAPIView(APIView):
    serializer_class = WaitListSerializer

    def get(self, request):
        try:
            waitlist = WaitList.objects.all()
        except WaitList.DoesNotExist:
            return Response({"error": "WaitList topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(waitlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
