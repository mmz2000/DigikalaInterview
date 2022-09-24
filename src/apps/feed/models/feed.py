from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Feed(models.Model):
    name = models.CharField(max_length=31, verbose_name=_("Name"))
    favorited_by = models.ManyToManyField(
        get_user_model(),
        verbose_name=_("Favorited By"),
        related_query_name="favorite_feeds",
    )
    rss_url = models.URLField(verbose_name=_("RSS URL"))
    max_saved_items = models.IntegerField(verbose_name=_("Max Saved Items"))
    refresh_rate = models.IntegerField(
        default=1,
        verbose_name=_("Refresh Rate"),
        choices=[
            (1, "1 hour"),
            (2, "2 hours"),
            (6, "6 hours"),
            (12, "12 hours"),
            (24, "1 day"),
        ],
    )

    class Meta:
        verbose_name = _("Feed")
        verbose_name_plural = _("Feeds")
