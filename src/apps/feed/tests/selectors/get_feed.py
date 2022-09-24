from django.test import TestCase

from src.apps.feed.selectors import get_feed_list
from src.apps.feed.tests.factories import FeedFactory, UserFactory


class GetFeedSelectorTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.favorited_feed = FeedFactory()
        self.not_favorited_feed = FeedFactory()
        self.favorited_feed.favorited_by.add(self.user)
        self.favorited_feed.save()

    def test_get_feed_list(self):
        feed_list = get_feed_list(user_id=self.user.id)
        self.assertEqual(len(feed_list), 2)
        self.assertEqual(feed_list[0].is_favorite, True)
        self.assertEqual(feed_list[0].id, self.favorited_feed.id)
        self.assertEqual(feed_list[1].is_favorite, False)
        self.assertEqual(feed_list[1].id, self.not_favorited_feed.id)
