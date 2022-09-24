from django.test import LiveServerTestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from src.api.tests.factories import FeedFactory, UserFactory
from src.apps.accounts.services import login_by_id
from src.errors import ErrorEnum


class RemoveFromFavoriteAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.user = UserFactory()
        self.favorite_feed = FeedFactory()
        self.favorite_feed.favorited_by.add(self.user)
        tokens = login_by_id(user_id=self.user.id)
        self.access_token = tokens.get("access_token")
        self.client = RequestsClient()

    def make_request(self, feed_id, headers=None):
        return self.client.delete(
            f"{self.live_server_url}/api/feed/{feed_id}/favorite/",
            headers=headers,
        )

    def test_ok_response(self):
        response = self.make_request(
            self.favorite_feed.id,
            headers={"Authorization": f"Bearer {self.access_token}"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json().get("ok"))
        self.assertIsNone(response.json().get("data"))
        self.assertFalse(
            self.favorite_feed.favorited_by.filter(id=self.user.id).exists()
        )

    def test_unauthorized_response(self):
        response = self.make_request(self.favorite_feed.id)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_not_found_response(self):
        response = self.make_request(
            0,
            headers={"Authorization": f"Bearer {self.access_token}"},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.json().get("ok"))
        self.assertEqual(
            response.json().get("error_type"),
            [ErrorEnum.RemoveFromFavoriteAPIView.FEED_NOT_FOUND],
        )
