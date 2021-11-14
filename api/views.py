import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ScheduleSerializer, MultiScheduleSerializer
from .models import ScheduleModel


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer


class CreateScheduleViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ScheduleModel.objects.all()
    serializer_class = MultiScheduleSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     ScheduleModel.objects.all().delete()
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        ScheduleModel.objects.all().delete()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)







