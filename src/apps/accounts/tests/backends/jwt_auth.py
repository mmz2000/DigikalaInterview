from django.test import TestCase
from rest_framework.test import APIRequestFactory

from src.apps.accounts.backends import JWTAuthentication
from src.apps.accounts.functions import login
from src.apps.accounts.tests.factories import UserFactory


class JWTAuthenticationBackendTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UserFactory()
        tokens = login(self.user)
        self.access = tokens.get("access_token")
        self.refresh = tokens.get("refresh_token")
        self.auth_class = JWTAuthentication()

    def test_jwt_auth_backend(self):
        def create_request(HTTP_ACCESS=None):
            return self.factory.get(
                "/examlple", data=None, HTTP_ACCESS=HTTP_ACCESS
            )

        request_fail = create_request()
        self.assertIsNone(self.auth_class.authenticate(request_fail))

        request_raise = create_request(HTTP_ACCESS="invalid")
        self.assertIsNone(self.auth_class.authenticate(request_raise))

        request_raise = create_request(HTTP_ACCESS=self.refresh)
        self.assertIsNone(self.auth_class.authenticate(request_raise))

        request_success = create_request(HTTP_ACCESS=self.access)
        self.assertEqual(
            self.auth_class.authenticate(request_success)[0], self.user
        )

        request_success = create_request(HTTP_ACCESS=f"Bearer {self.access}")
        self.assertEqual(
            self.auth_class.authenticate(request_success)[0], self.user
        )
