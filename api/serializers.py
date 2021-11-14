from abc import ABC

from .models import ScheduleModel
from rest_framework import serializers


class CustomScheduleSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        schedule = [ScheduleModel(**item) for item in validated_data]
        return ScheduleModel.objects.bulk_create(schedule)

class MultiScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields ='__all__'
        list_serializer_class = CustomScheduleSerializer

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = '__all__'
