from django.db import transaction

from src.apps.feed.models import Feed
from src.apps.feed.selectors import get_feed_by_id
from src.errors import ModelNotFoundException


@transaction.atomic
def add_favorite_feed(user_id, feed_id):
    try:
        feed = get_feed_by_id(feed_id=feed_id)
    except Feed.DoesNotExist:
        raise ModelNotFoundException()
    feed.favorited_by.add(user_id)


@transaction.atomic
def remove_favorite_feed(user_id, feed_id):
    try:
        feed = get_feed_by_id(feed_id=feed_id)
    except Feed.DoesNotExist:
        raise ModelNotFoundException()
    feed.favorited_by.remove(user_id)
