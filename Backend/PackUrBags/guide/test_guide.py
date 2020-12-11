from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from guide.api.views import *
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.test import TestCase
from guide.models import GuideData


class TestGuideUrls(APITestCase):
    def testForGuideList(self):
        path = reverse('GuideList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, GuideList.as_view().__name__)

    def testForGuideForAPlace(self):
        path = reverse('GuidePlace')
        found = resolve(path)
        self.assertEqual(found.func.__name__, GuidePlace.as_view().__name__)
    
    def testForGuideDetail(self):
        path = reverse('GuideDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, GuideDetail.as_view().__name__)



