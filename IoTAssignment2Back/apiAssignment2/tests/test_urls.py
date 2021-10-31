from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apiAssignment2.views import api_overview, get_items, get_item, insert_item, delete_item, update_item

class TestUrls(SimpleTestCase):
    def test_apiOverview_url_resolved(self):
        url = reverse('ApiOverview')
        self.assertEquals(resolve(url).func, api_overview)

    def test_getItems_url_resolved(self):
        url = reverse('getMoistureLevels')
        self.assertEquals(resolve(url).func, get_items)

    def test_getItem_url_resolved(self):
        url = reverse('getMoistureLevel', args=['1'])
        self.assertEquals(resolve(url).func, get_item)

    def test_insertItem_url_resolved(self):
        url = reverse('insertMoistureLevel')
        self.assertEquals(resolve(url).func, insert_item)
    
    def test_updateItem_url_resolved(self):
        url = reverse('updateMoistureLevel', args=['1'])
        self.assertEquals(resolve(url).func, update_item)

    def test_deleteItem_url_resolved(self):
        url = reverse('deleteMoistureLevel', args=['1'])
        self.assertEquals(resolve(url).func, delete_item)
