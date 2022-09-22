import faker
from django.test import LiveServerTestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from src.errors import SerializerErrors


class RegisterAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.faker = faker.Faker()

    def make_request(self, data):
        return self.client.post(
            f"{self.live_server_url}/api/accounts/sign-up/",
            json=data,
        )

    def test_bad_request_response(self):
        response = self.make_request({})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = response.json()
        error_type = response_data.get("error_type")
        self.assertSetEqual(
            set(error_type),
            set(SerializerErrors.create_user_serialzier.values()),
        )
        self.assertFalse(response_data.get("ok"))

    def test_created_response(self):
        data = {
            "username": self.faker.user_name(),
            "email": self.faker.email(),
            "password": "Along@cceptabl3pAssw8rd",
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
        }
        response = self.make_request(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()
        self.assertTrue(response_json.get("ok"))
        response_data = response_json.get("data")
        self.assertIn("access_token", response_data)
        self.assertIn("refresh_token", response_data)
        data.pop("password")
        response_data.pop("access_token")
        response_data.pop("refresh_token")
        self.assertDictEqual(response_data, data)
