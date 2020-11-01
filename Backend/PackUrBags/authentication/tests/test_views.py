from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.register_user_data = {
            "email": "testmail@packurbags.com",
            "username": "username",
            "first_name": "Test",
            "last_name": "Account",
            "phone_number": "9999999999",
            "password": "password@123"
        }
        self.login_user_data = {
            "email": "testmail@packurbags.com",
            "password": "password@123"
        }

    def test_register_view_post_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_register_view_post_data(self):
        response = self.client.post(self.register_url, self.register_user_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_login_view_post_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 400)

    def test_login_post_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        response = self.client.post(self.login_url, self.login_user_data, format="json")
        self.assertEqual(response.status_code, 200)
