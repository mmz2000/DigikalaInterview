from rest_framework import serializers

from src.apps.feed.models import Feed


class FeedListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Feed
        fields = ("id", "name", "rss_url", "max_saved_items", "is_favorite")

    def get_is_favorite(self, obj):
        if hasattr(obj, "is_favorite"):
            return obj.is_favorite
        user_id = self.context.get("user_id")
        if user_id is None:
            return False
        return obj.favorited_by.filter(id=user_id).exists()
