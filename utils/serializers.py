from rest_framework import serializers

from utils.models import WorkTime, HomepageStats, FooterStats, SocialMedia, Location, PhoneNumber, Email


class HomePageStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageStats
        fields = '__all__'


class FooterStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterStats
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = '__all__'
