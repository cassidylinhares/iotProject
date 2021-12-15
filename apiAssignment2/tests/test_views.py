from django.test import TestCase, Client
from django.urls import reverse
from apiAssignment2.models import Moisture

class TestViews(TestCase):
    #runs before each test
    def setUp(self):
        self.client = Client()

        self.moisturetest1 = Moisture.objects.create(level=0.78, plant_type='pothos')

        self.apiOverviewUrl = reverse('ApiOverview')
        self.getManyUrl = reverse('getMoistureLevels')
        self.getOneUrl = reverse('getMoistureLevel', args=['1'])
        self.create = reverse('insertMoistureLevel')
        self.update = reverse('updateMoistureLevel', args=['1'])
        self.delete = reverse('deleteMoistureLevel', args=['1'])

    def test_apiOverview(self):
        response = self.client.get(self.apiOverviewUrl)
        self.assertEquals(response.status_code, 200)

    def test_get_many(self):
        response = self.client.get(self.getManyUrl)
        self.assertEquals(response.status_code, 200)

    def test_get_one(self):
        response = self.client.get(self.getOneUrl)
        self.assertEquals(response.status_code, 200)

    def test_insert(self):
        response = self.client.post(self.create, {'level': 0.24, 'plant_type':'fern'})
        self.assertEquals(response.status_code, 201)
        self.assertEquals(str(Moisture.objects.last().level), '0.240')
        self.assertEquals(str(Moisture.objects.last().id), '2')

    def test_update(self):
        response = self.client.put(
            self.update, 
            data={
                'level': 0.14,
                'plant_type':'cactus'
            }, 
            content_type='application/json'
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(str(Moisture.objects.last().level), '0.140')
        self.assertEquals(str(Moisture.objects.last().id), '1')

    def test_delete(self):
        response = self.client.delete(self.delete)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Moisture.objects.count(), 0)
        
