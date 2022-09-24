from django.test import LiveServerTestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from src.api.tests.factories import FeedFactory, ItemFactory, UserFactory
from src.apps.accounts.services import login_by_id
from src.apps.feed.services import get_limited_item_list
from src.errors import ErrorEnum


class GetItemListAPIViewTestCase(LiveServerTestCase):
    def setUp(self):
        self.user = UserFactory()
        tokens = login_by_id(user_id=self.user.id)
        feed = FeedFactory()
        feed.favorited_by.add(self.user)
        feed.save()
        ItemFactory(feed=feed)
        ItemFactory.create_batch(5)
        self.access_token = tokens.get("access_token")
        self.client = RequestsClient()

    def make_request(self, headers=None, query_params=None):
        return self.client.get(
            f"{self.live_server_url}/api/feed/",
            headers=headers,
            params=query_params,
        )

    def test_ok_response(self):
        response = self.make_request(
            headers={"Authorization": f"Bearer {self.access_token}"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json().get("ok"))
        data = response.json().get("data")
        items, count = get_limited_item_list(self.user.id, 10, 0)
        items_from_response = data.get("items")
        count_from_response = data.get("count")
        self.assertListEqual(items, items_from_response)
        self.assertEqual(count, count_from_response)

    def test_unauthorized_response(self):
        response = self.make_request()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bad_request_response(self):
        response = self.make_request(
            headers={"Authorization": f"Bearer {self.access_token}"},
            query_params={"limit": "invalid", "offset": "invalid"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.json().get("ok"))
        self.assertListEqual(
            response.json().get("error_type"),
            [ErrorEnum.GetItemListAPIView.INVALID_LIMIT_OR_OFFSET],
        )

    def test_not_found_response(self):
        response = self.make_request(
            headers={"Authorization": f"Bearer {self.access_token}"},
            query_params={"limit": 10, "offset": 1000},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.json().get("ok"))
        self.assertListEqual(
            response.json().get("error_type"),
            [ErrorEnum.GetItemListAPIView.INVALID_LIMIT_OR_OFFSET],
        )
