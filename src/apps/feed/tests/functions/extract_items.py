from django.test import TestCase

from src.apps.feed.functions import extract_items
from src.apps.feed.tests.factories import FeedFactory


class ExtractItemsFunctionTestCase(TestCase):
    def setUp(self):
        self.feed = FeedFactory()
        self.fake_feed_data = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<rss version="2.0">'
            "<channel>"
            "<title>Sample Feed</title>"
            "<description>For documentation &lt;em&gt"
            ";only&lt;/em&gt;</description>"
            "<link>http://example.org/</link>"
            "<pubDate>Sat, 07 Sep 2002 00:00:01 GMT</pubDate>"
            "<!-- other elements omitted from this example -->"
            "<item>"
            "<title>First entry title</title>"
            "<link>http://example.org/entry/3</link>"
            '<description>Watch out for &lt;span style="background-image:'
            "url(javascript:window.location='http://example.org/')\"&gt;nasty "
            "tricks&lt;/span&gt;</description>"
            "<pubDate>Thu, 05 Sep 2002 00:00:01 GMT</pubDate>"
            "<guid>http://example.org/entry/3</guid>"
            "<!-- other elements omitted from this example -->"
            "</item>"
            "</channel>"
            "</rss>"
        )

    def test_extract_items(self):
        items = extract_items(self.fake_feed_data, self.feed.id)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "First entry title")
        self.assertEqual(items[0].url, "http://example.org/entry/3")
        self.assertEqual(
            items[0].content,
            "Watch out for <span>nasty tricks</span>",
        )
