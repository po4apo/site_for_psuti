from django.contrib import admin
from .models import ScheduleModel


class Schedule(admin.ModelAdmin):
    list_display =('id', 'weekday', 'st_group', 'odd_even')

admin.site.register(ScheduleModel, Schedule)
