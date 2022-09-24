from src.apps.feed.selectors import (
    get_limited_item_list as get_limited_item_list_selector,
)
from src.apps.feed.serializers import ItemListSerializer


def get_limited_item_list(user_id, limit, offset):
    query_set, count = get_limited_item_list_selector(
        user_id=user_id, limit=limit, offset=offset
    )
    return (
        ItemListSerializer(
            query_set,
            many=True,
            context={"user_id": user_id},
        ).data,
        count,
    )
