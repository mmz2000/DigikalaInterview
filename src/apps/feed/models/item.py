from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.feed.models.feed import Feed


class Item(models.Model):
    title = models.CharField(max_length=63, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    url = models.URLField(verbose_name=_("URL"))
    feed = models.ForeignKey(
        Feed,
        on_delete=models.CASCADE,
        verbose_name=_("Feed"),
        related_name="items",
    )
    published_at = models.DateTimeField(verbose_name=_("Published At"))

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
