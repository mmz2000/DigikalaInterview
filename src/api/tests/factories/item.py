from datetime import timedelta

import factory
import factory.fuzzy
from django.utils import timezone

from src.api.tests.factories.feed import FeedFactory


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "feed.Item"

    title = factory.Faker("word")
    content = factory.Faker("paragraph")
    url = factory.Faker("url")
    published_at = factory.fuzzy.FuzzyDateTime(
        timezone.now() - timedelta(days=365), timezone.now()
    )
    feed = factory.SubFactory(FeedFactory)
