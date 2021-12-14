from django.urls import path
from graphical_interface.views import ScheduleViewList, ReportFormViewList

urlpatterns = [
    path('', ScheduleViewList.as_view(), name = 'main'),
    path('report/', ReportFormViewList.as_view(), name = 'report_page'),
]