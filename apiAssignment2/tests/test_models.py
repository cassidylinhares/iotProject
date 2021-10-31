from django.test import TestCase
from apiAssignment2.models import Moisture

class TestMoistureModel(TestCase):
    def setUp(self):
        self.test1 = Moisture.objects.create(level=0.21)

    def test_test1_is_assigned(self):
        self.assertEquals(self.test1.level, 0.21)