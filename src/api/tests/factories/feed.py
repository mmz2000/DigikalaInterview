import factory


class FeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "feed.Feed"

    name = factory.Faker("word")
    rss_url = factory.Faker("url")
    max_saved_items = factory.Faker("pyint")
