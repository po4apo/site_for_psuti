
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from api.models import ScheduleModel, ReportModel
from graphical_interface.forms import ChooseGroup, ReportForm


class ScheduleViewList(FormMixin, ListView):
    model = ScheduleModel
    template_name = 'main.html'
    form_class = ChooseGroup



    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request):
        queryset = ScheduleModel.objects.filter(Q(st_group__contains=[request.GET.get('st_group')]) & (Q(odd_even= request.GET.get('odd_even')) | Q(odd_even= 'full'))).order_by('weekday', 'sub_time')
        self.initial = {'st_group': request.GET.get('st_group'), 'odd_even':request.GET.get('odd_even')}
        self.object_list = queryset
        context = self.get_context_data()
        return self.render_to_response(context)


class ReportFormViewList(FormMixin, ListView):
    model = ReportModel
    template_name = 'report_form.html'
    form_class = ReportForm
    success_url = '/123'


    def get(self, request):
        data = request.GET
        print(data)
        self.initial = data
        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data())
