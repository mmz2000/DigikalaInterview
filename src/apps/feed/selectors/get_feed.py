from django.db.models import BooleanField, Case, When

from src.apps.feed.models import Feed


def get_feed_list(user):
    return Feed.objects.annotate(
        is_favorite=Case(
            When(favorited_by=user, then=True),
            default=False,
            output_field=BooleanField(),
        )
    ).order_by("-is_favorite", "id")
