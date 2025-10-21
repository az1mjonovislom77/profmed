from rest_framework import serializers

from waitlist.models import WaitList


class WaitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitList
        fields = '__all__'
