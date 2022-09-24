from src.apps.feed.selectors import get_feed_list as get_feed_list_selector
from src.apps.feed.serializers import FeedListSerializer


def get_feed_list(user_id):
    return FeedListSerializer(
        get_feed_list_selector(user_id=user_id),
        many=True,
        context={"user_id": user_id},
    ).data
