from django.test import TestCase

from src.apps.feed.services import get_feed_list
from src.apps.feed.tests.factories import FeedFactory, UserFactory


class GetFeedServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.favorited_feed = FeedFactory()
        self.not_favorited_feed = FeedFactory()
        self.favorited_feed.favorited_by.add(self.user)
        self.favorited_feed.save()

    def test_get_feed_list_service(self):
        feed_list = get_feed_list(user_id=self.user.id)
        self.assertEqual(len(feed_list), 2)
        self.assertEqual(feed_list[0].get("is_favorite"), True)
        self.assertEqual(feed_list[0].get("name"), self.favorited_feed.name)
        self.assertEqual(feed_list[1].get("is_favorite"), False)
        self.assertEqual(
            feed_list[1].get("name"), self.not_favorited_feed.name
        )
