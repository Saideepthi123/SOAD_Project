from rest_framework.test import APITestCase
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from authentication.models import UserData
from rest_framework.authtoken.models import Token


class TestAuthenticationViews(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.google_auth_url = reverse('google-auth')
        self.logout_url = reverse('logout')
        self.token = ""
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

    def test_login_view_post_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        response = self.client.post(self.login_url, self.login_user_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_login_view_post_data_when_user_session_exists(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        self.client.post(self.login_url, self.login_user_data, format="json")
        response = self.client.post(self.login_url, self.login_user_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_home_view_get(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_google_auth_view_get_when_user_logged_in(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        self.client.post(self.login_url, self.login_user_data, format="json")
        response = self.client.get(self.google_auth_url)
        self.assertEqual(response.status_code, 400)

    def test_google_auth_view_get_when_user_not_logged_in(self):
        response = self.client.get(self.google_auth_url)
        self.assertEqual(response.status_code, 302)

    def test_logout_view_get_when_user_logged_in(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        self.client.post(self.login_url, self.login_user_data, format="json")
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)

    def test_logout_view_get_when_user_not_logged_in(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 400)

    def test_verify_email_get(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        email = self.register_user_data['email']
        user = UserData.objects.get(email=email)
        self.token = Token.objects.get(user=user)
        uidb64 = urlsafe_base64_encode(smart_bytes(user.user_id))
        verify_email_url = reverse('email-verify', kwargs={'uidb64': uidb64})
        response = self.client.get(verify_email_url)
        self.test_api_authentication()
        self.assertEqual(response.status_code, 200)

    def test_api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))
