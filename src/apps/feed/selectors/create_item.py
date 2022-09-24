from django.db import transaction

from src.apps.feed.models import Item


@transaction.atomic
def create_item_batch(items: list) -> None:
    print(items)
    Item.objects.bulk_create(items)
