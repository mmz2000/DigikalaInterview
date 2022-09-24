from django.urls import path

from src.api.views.feed import GetFeedListAPIView

urlpatterns = [
    path("all/", GetFeedListAPIView.as_view(), name="feed_list"),
]
