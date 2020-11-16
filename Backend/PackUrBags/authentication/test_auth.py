import pytest
from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from authentication.api.views import RegisterView, LoginAPIView, LogoutView, VerifyEmail, \
    RequestPasswordResetEmail, PasswordTokenCheckAPI, PasswordReset, GoogleAuthentication, HomeView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate
from django.test import TestCase
from authentication.models import UserData


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class UserTest(TestCase):
    pytestmark = pytest.mark.django_db

    def setUp(self):
        self.username = "packurbags"
        self.password = "packurbags"
        self.email = "packurbags@packurbags.com"
        self.first_name = "packurbags"
        self.last_name = "tourism"
        self.phone_number = "8888888888"

        self.user = UserData.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number
        )
        self.user.save()

    def test_correct(self):
        user = authenticate(username="packurbags", password="packurbags")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username="testpackurbags", password="packurbags")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username="testuser", password="pass")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_user_permission(self):
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)


class TestAuthenticationUrls(APITestCase):
    pytestmark = pytest.mark.django_db

    def test_register_url_is_resolved(self):
        path = reverse('register')
        found = resolve(path)
        self.assertEqual(found.func.__name__, RegisterView.as_view().__name__)

    def test_login_url_is_resolved(self):
        path = reverse('login')
        found = resolve(path)
        self.assertEqual(found.func.__name__, LoginAPIView.as_view().__name__)

    def test_logout_url_is_resolved(self):
        path = reverse('logout')
        found = resolve(path)
        self.assertEqual(found.func.__name__, LogoutView.as_view().__name__)

    def test_email_verify_url_is_resolved(self):
        path = reverse('email-verify', args=['some-uidb'])
        found = resolve(path)
        self.assertEqual(found.func.__name__, VerifyEmail.as_view().__name__)

    def test_request_reset_email_url_is_resolved(self):
        path = reverse('request-reset-email')
        found = resolve(path)
        self.assertEqual(found.func.__name__, RequestPasswordResetEmail.as_view().__name__)

    def test_password_reset_confirm_url_is_resolved(self):
        path = reverse('password-reset-confirm', args=['some-uidb', 'some-token'])
        found = resolve(path)
        self.assertEqual(found.func.__name__, PasswordTokenCheckAPI.as_view().__name__)

    def test_reset_password_url_is_resolved(self):
        path = reverse('reset-password', args=['1'])
        found = resolve(path)
        self.assertEqual(found.func.__name__, PasswordReset.as_view().__name__)

    def test_google_authentication_url_is_resolved(self):
        path = reverse('google-auth')
        found = resolve(path)
        self.assertEqual(found.func.__name__, GoogleAuthentication.as_view().__name__)

    def test_google_auth_redirect_url_is_resolved(self):
        path = reverse('home')
        found = resolve(path)
        self.assertEqual(found.func.__name__, HomeView.as_view().__name__)


class TestAuthenticationViews(APITestCase):
    pytestmark = pytest.mark.django_db

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.google_auth_url = reverse('google-auth')
        self.logout_url = reverse('logout')
        self.request_pwd_reset_email = reverse('request-reset-email')
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
        self.request_pwd_reset_email_data = {
            "email": "testmail@packurbags.com"
        }
        self.password_reset_data = {
            "password1": "newpassword@123",
            "password2": "newpassword@123"
        }

    def test_register_view_post_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_register_view_post_data(self):
        response = self.client.post(self.register_url, self.register_user_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_login_view_post_no_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
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

    def test_request_password_reset_email_view_post_no_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        response = self.client.post(self.request_pwd_reset_email)
        self.assertEqual(response.status_code, 400)

    def test_request_password_reset_email_view_post_with_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        response = self.client.post(self.request_pwd_reset_email, self.request_pwd_reset_email_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_password_reset_view_with_no_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        email = self.register_user_data['email']
        user = UserData.objects.get(email=email)
        user_id = user.user_id
        password_reset_url = reverse('reset-password', kwargs={'user_id': user_id})
        response = self.client.post(password_reset_url)
        self.assertEqual(response.status_code, 400)

    def test_password_reset_view_with_data(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        email = self.register_user_data['email']
        user = UserData.objects.get(email=email)
        user_id = user.user_id
        password_reset_url = reverse('reset-password', kwargs={'user_id': user_id})
        response = self.client.post(password_reset_url, self.password_reset_data, format="json")
        self.assertEqual(response.status_code, 302)

    def test_password_token_check_view_get(self):
        self.client.post(self.register_url, self.register_user_data, format="json")
        email = self.register_user_data['email']
        user = UserData.objects.get(email=email)
        user.id = user.user_id
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        password_token_check_url = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
        response = self.client.get(password_token_check_url)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        return super().tearDown()
