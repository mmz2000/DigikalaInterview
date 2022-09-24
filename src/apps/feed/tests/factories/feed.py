import factory

from src.apps.feed.models import Feed


class FeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Feed

    name = factory.Faker("word")
    rss_url = factory.Faker("url")
    max_saved_items = factory.Faker("pyint")
