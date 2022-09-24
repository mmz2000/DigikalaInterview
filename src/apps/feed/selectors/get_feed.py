from django.db.models import BooleanField, Case, When

from src.apps.feed.models import Feed


def get_feed_list(user_id):
    return Feed.objects.annotate(
        is_favorite=Case(
            When(favorited_by__id=user_id, then=True),
            default=False,
            output_field=BooleanField(),
        )
    ).order_by("-is_favorite", "id")


def get_feed_by_id(feed_id):
    return Feed.objects.get(id=feed_id)
