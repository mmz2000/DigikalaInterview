import random

import faker
from django.test import TestCase

from src.apps.accounts.services import login, login_by_id
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

    def test_login_by_id_service(self):
        data = login_by_id(user_id=self.user.id)
        self.assertIsInstance(data, dict)
        self.assertIn("access_token", data)
        self.assertIn("refresh_token", data)
        data = login_by_id(user_id=random.randint(1000, 10000))
        self.assertIsNone(data)
