from django.test import TestCase

from src.apps.feed.services import add_favorite_feed, remove_favorite_feed
from src.apps.feed.tests.factories import FeedFactory, UserFactory
from src.errors import ModelNotFoundException


class FavoriteServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.feed = FeedFactory()

    def test_add_favorite_feed_service(self):
        add_favorite_feed(self.user.id, self.feed.id)
        self.assertIn(self.user, self.feed.favorited_by.all())
        with self.assertRaises(ModelNotFoundException):
            add_favorite_feed(self.user.id, 0)

    def test_remove_favorite_feed_service(self):
        add_favorite_feed(self.user.id, self.feed.id)
        remove_favorite_feed(self.user.id, self.feed.id)
        self.assertNotIn(self.user, self.feed.favorited_by.all())
        with self.assertRaises(ModelNotFoundException):
            remove_favorite_feed(self.user.id, 0)
