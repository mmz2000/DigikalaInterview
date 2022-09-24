from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from src.apps.feed.functions import extract_items
from src.apps.feed.selectors import create_item_batch, get_feed_list


class Command(BaseCommand):
    help = "Check for updates"

    @transaction.atomic
    def handle(self, *args, **options):
        now_hour = timezone.now().hour
        for feed in get_feed_list():
            if not now_hour % feed.refresh_rate:
                continue
            items = extract_items(feed.url, feed.id)
            create_item_batch(feed, items)
            max_items = feed.max_items
            feed.items.order_by("-published_at")[max_items:].delete()
