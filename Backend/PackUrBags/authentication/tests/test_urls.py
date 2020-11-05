from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from authentication.api.views import RegisterView, LoginAPIView, LogoutView, VerifyEmail, \
    RequestPasswordResetEmail, PasswordTokenCheckAPI, PasswordReset, GoogleAuthentication, HomeView


class TestAuthenticationUrls(APITestCase):

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
