from django.contrib.postgres.fields import ArrayField
from django.db import models

class ScheduleModel(models.Model):
    department = models.CharField(max_length=100,
                          null=True,
                          blank=True)                 #: "ВМ",
    teacher_name = models.CharField(max_length=100,
                          null=True,
                          blank=True)               #: "Плотников А.Н.",
    weekday = models.CharField(max_length=100,
                          null=True,
                          blank=True)                    # нужно вынести в отдельную таблицу: "mon",
    sub_time = models.TimeField(null=True,
                          blank=True)                                 #: "8:10",
    sub_name = models.CharField(max_length=100,
                          null=True,
                          blank=True)                   #: "СРМ пр. чет.",
    sub_type = models.CharField(max_length=100,
                          null=True,
                          blank=True)                   # нужно вынести в отдельную таблицу: "пр",
    st_group = ArrayField(models.CharField(max_length=100),
                          null=True,
                          blank=True)       #: ["ИКТ-05"],
    au_number = ArrayField(models.CharField(max_length=100,
                          null=True,
                          blank=True),
                           null=True,
                           blank=True)                  #: "а. 8-02",
    odd_even = models.CharField(max_length=100,
                          null=True,
                          blank=True)                  # нужно вынести в отдельную таблицу: "чет"

    def __str__(self):
        return self.sub_name


class ReportModel(models.Model):
    description = models.TextField(verbose_name='Описание проблемы',)
    st_group = models.CharField(max_length=100,
                                verbose_name="Название группы")
    odd_even = models.CharField(max_length=5,
                                choices=[('even', 'чёт'), ('odd', 'нечёт')],
                                verbose_name='Чётность')


    def __str__(self):
        return self.st_group