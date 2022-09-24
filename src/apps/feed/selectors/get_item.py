from django.db.models import BooleanField, Case, When

from src.apps.feed.models import Item


def get_limited_item_list(
    user_id: int, limit: int = 10, offset: int = 0
) -> list:
    items = Item.objects.annotate(
        is_favorite=Case(
            When(feed__favorited_by__id=user_id, then=True),
            default=False,
            output_field=BooleanField(),
        )
    ).order_by("-is_favorite", "-published_at")
    end = offset + limit
    return items[offset:end], items.count()
