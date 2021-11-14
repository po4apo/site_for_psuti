from django.test import TestCase
from .models import ScheduleModel


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        ScheduleModel.objects.create(
        department = "ВМ",
        teacher_name = "Алашеева Е.А.",
        weekday = "thu",
        sub_time = '9:10:00',
        sub_name = "ДМ  лк.  чет",
        sub_type = "лк",
        st_group = [
            "УИ-01",
            "ПИ-01",
            "УИТС-01",
            "РПИС-01",
            "РПИС-03",
            "РПИС-02"
        ],
        au_number = "а. 2-10",
        odd_even = "чет"
    )
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_model(self):
        print("Method: test_model.")
        print(ScheduleModel.objects.all()[0].st_group)
        self.assertFalse(False)
