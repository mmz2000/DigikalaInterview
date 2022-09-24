from datetime import datetime, timezone
from time import mktime

import feedparser

from src.apps.feed.models import Item


def extract_items(feed_url, feed_id):
    feed = feedparser.parse(feed_url)
    items = []
    for entry in feed.entries:
        item = Item()
        item.title = entry.title
        item.url = entry.link
        item.content = entry.description
        item.published_at = datetime.fromtimestamp(
            mktime(entry.published_parsed)
        ).replace(tzinfo=timezone.utc)
        item.feed_id = feed_id
        items.append(item)
    return items
