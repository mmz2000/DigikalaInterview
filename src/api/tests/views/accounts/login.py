from django.test import LiveServerTestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from src.api.tests.factories import UserFactory
from src.errors import ErrorEnum


class LoginAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.user = UserFactory()

    def make_request(self, data):
        return self.client.post(
            f"{self.live_server_url}/api/accounts/sign-in/",
            json=data,
        )

    def test_bad_request_response(self):
        response = self.make_request({})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertListEqual(
            response.json().get("error_type"),
            [ErrorEnum.LoginAPIView.INVALID_CREDENTIALS],
        )

    def test_ok_response(self):
        data = {
            "authenticator": self.user.email,
            "password": "foo",
        }
        response = self.make_request(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertTrue(response_json.get("ok"))
        response_data = response_json.get("data")
        self.assertIn("access_token", response_data)
        self.assertIn("refresh_token", response_data)
