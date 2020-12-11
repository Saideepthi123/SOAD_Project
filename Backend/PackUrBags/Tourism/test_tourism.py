from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from Tourism.api.views import *
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.test import TestCase
from Tourism.models import UserData, Booking, UserHistory


class TestTourismUrls(APITestCase):
    def testForUserList(self):
        path = reverse('UserList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, UserList.as_view().__name__)

    def testForUserDetail(self):
        path = reverse('UserDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, UserDetail.as_view().__name__)

    def testForBookingDetailUser(self):
        path = reverse('BookingDetailUser', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, BookingDetailUser.as_view().__name__)

    def testForBookingDetailGuide(self):
        path = reverse('BookingDetailGuide', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, BookingDetailGuide.as_view().__name__)

    def testForBookingDetail(self):
        path = reverse('BookingDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, BookingDetail.as_view().__name__)

    def testForBookingList(self):
        path = reverse('BookingList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, BookingList.as_view().__name__)


    def testForPaymentDetailUser(self):
        path = reverse('PaymentDetailUser', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, PaymentDetailUser.as_view().__name__)

    def testForPaymentDetailGuide(self):
        path = reverse('PaymentDetailGuide', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, PaymentDetailGuide.as_view().__name__)

    def testForPaymentDetail(self):
        path = reverse('PaymentDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, PaymentDetail.as_view().__name__)

    def testForPaymentList(self):
        path = reverse('PaymentList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, PaymentList.as_view().__name__)

    def testForUserHistoryDetailUser(self):
        path = reverse('UserHistoryDetailUser', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, UserHistoryDetailUser.as_view().__name__)

    def testForUserHistoryDetail(self):
        path = reverse('UserHistoryDetail', args={'slug':1})
        found = resolve(path)
        self.assertEqual(found.func.__name__, UserHistoryDetail.as_view().__name__)

    def testForUserHistoryList(self):
        path = reverse('UserHistoryList')
        found = resolve(path)
        self.assertEqual(found.func.__name__, UserHistoryList.as_view().__name__)

    
    
    


