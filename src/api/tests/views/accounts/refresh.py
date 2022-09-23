from django.test import LiveServerTestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from src.api.tests.factories import UserFactory
from src.apps.accounts.services import login_by_id
from src.errors import ErrorEnum


class RefreshAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        user = UserFactory()
        tokens = login_by_id(user_id=user.id)
        self.refresh_token = tokens.get("refresh_token")
        self.client = RequestsClient()

    def make_request(self, data):
        return self.client.post(
            f"{self.live_server_url}/api/accounts/refresh/",
            json=data,
        )

    def test_bad_request_response(self):
        response = self.make_request({})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_type = response.json().get("error_type")
        self.assertListEqual(
            error_type, [ErrorEnum.RefreshAPIView.EMPTY_REFRESH]
        )
        response = self.make_request({"refresh_token": "invalid"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_type = response.json().get("error_type")
        self.assertListEqual(
            error_type, [ErrorEnum.RefreshAPIView.INVALID_REFRESH_TOKEN]
        )

    def test_ok_response(self):
        response = self.make_request({"refresh_token": self.refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertTrue(response_json.get("ok"))
        response_data = response_json.get("data")
        self.assertIn("access_token", response_data)
        self.assertIn("refresh_token", response_data)
