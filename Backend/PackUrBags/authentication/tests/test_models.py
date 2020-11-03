from django.contrib.auth import authenticate
from django.test import TestCase
from authentication.models import UserData


class UserTest(TestCase):
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
