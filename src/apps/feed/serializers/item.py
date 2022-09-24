from rest_framework import serializers

from src.apps.feed.models import Item
from src.apps.feed.serializers.feed import FeedNestedSerializer


class ItemListSerializer(serializers.ModelSerializer):
    feed = FeedNestedSerializer()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            "title",
            "content",
            "url",
            "feed",
            "published_at",
            "is_favorite",
        )

    def get_is_favorite(self, obj):
        if hasattr(obj, "is_favorite"):
            return obj.is_favorite
        user_id = self.context.get("user_id")
        if user_id is None:
            return False
        return obj.feed.favorited_by.filter(id=user_id).exists()
