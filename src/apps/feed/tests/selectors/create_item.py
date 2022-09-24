from django.test import TestCase

from src.apps.feed.models import Item
from src.apps.feed.selectors import create_item_batch
from src.apps.feed.tests.factories import FeedFactory, ItemFactory


class CreateItemSelectorTestCase(TestCase):
    def setUp(self):
        self.feed = FeedFactory()

    def test_create_item_batch_selector(self):
        items = ItemFactory.build_batch(5, feed=self.feed)
        self.assertEqual(Item.objects.count(), 0)
        create_item_batch(items)
        self.assertEqual(Item.objects.count(), 5)
