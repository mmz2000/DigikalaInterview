from rest_framework.permissions import IsAuthenticated

from src.api.views.feed.add_favorite import AddToFavoriteAPIView
from src.api.views.feed.get_feed_list import GetFeedListAPIView
from src.api.views.feed.get_item_list import GetItemListAPIView
from src.api.views.feed.remove_favorite import RemoveFromFavoriteAPIView


class FavoriteAPIView(AddToFavoriteAPIView, RemoveFromFavoriteAPIView):
    permission_classes = (IsAuthenticated,)
