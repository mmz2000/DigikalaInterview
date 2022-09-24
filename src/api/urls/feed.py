from django.urls import path

from src.api.views.feed import GetFeedListAPIView, GetItemListAPIView

urlpatterns = [
    path("", GetItemListAPIView.as_view(), name="item"),
    path("all/", GetFeedListAPIView.as_view(), name="feed_list"),
]
