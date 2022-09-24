from django.test import LiveServerTestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from src.api.tests.factories import FeedFactory, UserFactory
from src.apps.accounts.services import login_by_id
from src.apps.feed.services import get_feed_list


class GetFeedListAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.user = UserFactory()
        favorited_feed = FeedFactory()
        FeedFactory()
        favorited_feed.favorited_by.add(self.user)
        tokens = login_by_id(user_id=self.user.id)
        self.access_token = tokens.get("access_token")
        self.client = RequestsClient()

    def test_ok_response(self):
        response = self.client.get(
            f"{self.live_server_url}/api/feed/all/",
            headers={"Authorization": f"Bearer {self.access_token}"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json().get("ok"))
        data = response.json().get("data")
        self.assertListEqual(data, get_feed_list(self.user.id))

    def test_unauthorized_response(self):
        response = self.client.get(f"{self.live_server_url}/api/feed/all/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
