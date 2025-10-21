from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.models import HomepageStats, FooterStats, SocialMedia, Location, PhoneNumber, Email, WorkTime
from utils.serializers import HomePageStatsSerializer, FooterStatsSerializer, SocialMediaSerializer, LocationSerializer, \
    PhoneNumberSerializer, EmailSerializer, WorkTimeSerializer


@extend_schema(tags=["HomepageStats"], request=HomePageStatsSerializer, responses=HomePageStatsSerializer)
class HomepageStatsAPIView(APIView):
    serializer_class = HomePageStatsSerializer

    def get(self, request):
        homepage = HomepageStats.objects.all()
        serializer = HomePageStatsSerializer(homepage, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomePageStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['FooterStats'], request=FooterStatsSerializer, responses=FooterStatsSerializer)
class FooterStatsAPIView(APIView):
    serializer_class = FooterStatsSerializer

    def get(self, request):
        try:
            footer = FooterStats.objects.all()
        except FooterStats.DoesNotExist:
            return Response({"error": "FooterStats topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(footer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['SocialMedia'], request=SocialMediaSerializer, responses=SocialMediaSerializer)
class SocialMediaAPIView(APIView):
    serializer_class = SocialMediaSerializer

    def get(self, request):
        try:
            socialmedia = SocialMedia.objects.all()
        except SocialMedia.DoesNotExist:
            return Response({"error": "SocialMedia topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(socialmedia, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Location'], request=LocationSerializer, responses=LocationSerializer)
class LocationAPIView(APIView):
    serializer_class = LocationSerializer

    def get(self, request):
        try:
            location = Location.objects.all()
        except Location.DoesNotExist:
            return Response({"error": "Location topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(location, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['PhoneNumber'], request=PhoneNumberSerializer, responses=PhoneNumberSerializer)
class PhoneNumberAPIView(APIView):
    serializer_class = PhoneNumberSerializer

    def get(self, request):
        try:
            phonenumber = PhoneNumber.objects.all()
        except PhoneNumber.DoesNotExist:
            return Response({"error": "PhoneNumber topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(phonenumber, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Email'], request=EmailSerializer, responses=EmailSerializer)
class EmailAPIView(APIView):
    serializer_class = EmailSerializer

    def get(self, request):
        try:
            email = Email.objects.all()
        except Email.DoesNotExist:
            return Response({"error": "Email topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(email, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['WorkTime'], request=WorkTimeSerializer, responses=WorkTimeSerializer)
class WorkTimeAPIView(APIView):
    serializer_class = WorkTimeSerializer

    def get(self, request):
        try:
            worktime = WorkTime.objects.all()
        except WorkTime.DoesNotExist:
            return Response({"error": "WorkTime topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(worktime, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
