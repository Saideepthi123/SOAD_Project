from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from monuments.api.views import *
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.test import TestCase
from monuments.models import Monument, City, MonumentInfo



class TestMonumentsUrls(APITestCase):
    def testForMonumentList(self):
        path = reverse('MonumentList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, MonumentList.as_view().__name__)

    def testForMonumentDetail(self):
        path = reverse('MonumentDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, MonumentDetail.as_view().__name__)

    def testForMonumentInfoList(self):
        path = reverse('MonumentInfoList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, MonumentInfoList.as_view().__name__)
    
    def testForMonumentInfoDetail(self):
        path = reverse('MonumentInfoDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, MonumentInfoDetail.as_view().__name__)

    def testForCityList(self):
        path = reverse('CityList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, CityList.as_view().__name__)

    def testForCityDetail(self):
        path = reverse('CityDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, CityDetail.as_view().__name__)
    
    def testForMonumentsListofACity(self):
        path = reverse('MonumentsListofACity', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, MonumentInfoWithCityID.as_view().__name__)

    