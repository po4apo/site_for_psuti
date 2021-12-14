from collections import Iterable


from django import forms
from numpy.compat import basestring

from api.models import ScheduleModel, ReportModel


def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, basestring):
            for x in flatten(item):
                yield x
        else:
            yield (item, item)


class ChooseGroup(forms.Form):
    groups = list(set(flatten(ScheduleModel.objects.values_list('st_group'))))
    st_group = forms.MultipleChoiceField(choices=(groups),
                                         widget=forms.Select(attrs={'class': "form-select"}),
                                         label='Группа'

                                         )
    odd_even = forms.MultipleChoiceField(choices=[('even', 'чёт'), ('odd', 'нечёт')],
                                         widget=forms.Select(attrs={'class': "form-select"}),
                                         label='Чётность', )


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class':'form-control'}),
            'odd_even': forms.Select(attrs={'class': "form-select"}),
            'st_group': forms.TextInput(attrs={'class':'input-group'})

        }