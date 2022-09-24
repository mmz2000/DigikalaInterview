from rest_framework import serializers

from src.apps.feed.models import Item
from src.apps.feed.serializers.feed import FeedNestedSerializer


class ItemListSerializer(serializers.ModelSerializer):
    feed = FeedNestedSerializer()

    class Meta:
        model = Item
        fields = ("title", "content", "url", "feed", "published_at")
