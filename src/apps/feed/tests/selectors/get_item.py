from django.test import TestCase

from src.apps.feed.selectors import get_limited_item_list
from src.apps.feed.tests.factories import FeedFactory, ItemFactory, UserFactory


class GetItemSelectorTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        feed = FeedFactory()
        feed.favorited_by.add(self.user)
        feed.save()
        self.favorited_item = ItemFactory(feed=feed)
        self.other_items = ItemFactory.create_batch(5)

    def test_get_limited_item_list_selector(self):
        items, count = get_limited_item_list(self.user.id, limit=1, offset=0)
        self.assertEqual(len(items), 1)
        self.assertEqual(count, 6)
        item = items[0]
        self.assertTrue(hasattr(item, "is_favorite"))
        self.assertTrue(item.is_favorite)
        self.assertEqual(self.favorited_item, item)
