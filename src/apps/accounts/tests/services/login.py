import faker
from django.test import TestCase

from src.apps.accounts.services import login
from src.apps.accounts.tests.factories import UserFactory


class LoginServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.faker = faker.Faker()

    def test_login_service(self):
        data = login(authenticator=self.user.username, password="foo")
        self.assertIsInstance(data, dict)
        self.assertIn("access_token", data)
        self.assertIn("refresh_token", data)
        data = login(authenticator=self.user.email, password="foo")
        self.assertIsInstance(data, dict)
        self.assertIn("access_token", data)
        self.assertIn("refresh_token", data)
        data = login(authenticator=self.user.email, password="bar")
        self.assertIsNone(data)
        data = login(authenticator=self.faker.email(), password="foo")
        self.assertIsNone(data)
