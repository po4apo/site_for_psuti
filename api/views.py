import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ScheduleSerializer, MultiScheduleSerializer, ListScheduleSerializer
from .models import ScheduleModel


class ScheduleViewSet(viewsets.ViewSet):
    '''
    Фильтрует все записи по названию группы
    '''
    def list(self, request, pk = None):
        queryset = ScheduleModel.objects.filter(st_group__contains=[pk])
        serializer = ScheduleSerializer(queryset, many = True)
        return Response(serializer.data)


class CreateScheduleViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    Класс для полного обновления базы даннных.
    Старые данные удаляются!!!
    На их место загружаются новые
    '''
    queryset = ScheduleModel.objects.all()
    serializer_class = MultiScheduleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        ScheduleModel.objects.all().delete()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)












