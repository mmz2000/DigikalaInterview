from django.urls import path

from src.api.views.feed import (
    FavoriteAPIView,
    GetFeedListAPIView,
    GetItemListAPIView,
)

urlpatterns = [
    path("", GetItemListAPIView.as_view(), name="item"),
    path("all/", GetFeedListAPIView.as_view(), name="feed_list"),
    path(
        "<int:feed_id>/favorite/", FavoriteAPIView.as_view(), name="favorite"
    ),
]
