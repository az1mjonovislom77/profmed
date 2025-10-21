from django.shortcuts import get_object_or_404
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from doctor.models import Doctor
from doctor.serializers import DoctorSerializer


@extend_schema(tags=['Doctor'])
class DoctorAPIView(APIView):
    serializer_class = DoctorSerializer

    def get(self, request):
        try:
            doctor = Doctor.objects.all()
        except Doctor.DoesNotExist:
            return Response({"error": "Doctorlar topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @extend_schema(tags=['DoctorDetail'])
# class DoctorDetailAPIView(APIView):
#     serializer_class = DoctorSerializer
#
#     def get(self, request, pk):
#         doctor = get_object_or_404(Doctor, pk=pk)
#         serializer = DoctorSerializer(doctor, context={'request': request})
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         doctor = get_object_or_404(Doctor, pk=pk)
#         serializer = DoctorSerializer(doctor, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         doctor = get_object_or_404(Doctor, pk=pk)
#         doctor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
