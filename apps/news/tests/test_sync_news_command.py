from django.core.management import call_command
from django.test import TestCase
from unittest.mock import patch, Mock

from apps.news.models import Article


MOCK_API_RESPONSE = {
    "results": [
        {
            "id": 1,
            "title": "NASA studies Mars surface",
            "news_site": "NASA",
            "summary": "Some summary",
            "url": "https://nasa.gov/mars",
            "image_url": "https://img.nasa.gov/mars.jpg",
            "published_at": "2025-12-19T04:00:00Z",
        },
        {
            "id": 2,
            "title": "SpaceX launches new rocket",
            "news_site": "SpaceX",
            "summary": "Should be ignored",
            "url": "https://spacex.com",
            "image_url": "https://img.spacex.com/rocket.jpg",
            "published_at": "2025-12-19T04:00:00Z",
        },
        {
            "id": 3,
            "title": "NASA prepares Moon mission",
            "news_site": "NASA",
            "summary": "Moon mission",
            "url": "https://nasa.gov/moon",
            "image_url": "https://img.nasa.gov/moon.jpg",
            "published_at": "2025-12-19T04:00:00Z",
        },
    ]
}


class SyncNewsCommandTest(TestCase):

    @patch("apps.news.services.requests.get")
    def test_sync_news_filters_and_sentiment(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = MOCK_API_RESPONSE
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        call_command("sync_news", limit=5)

        articles = Article.objects.all()

        self.assertEqual(articles.count(), 2)

        titles = [a.title for a in articles]
        self.assertNotIn("SpaceX launches new rocket", titles)

        mars = Article.objects.get(title__icontains="Mars")
        moon = Article.objects.get(title__icontains="Moon")

        self.assertEqual(mars.sentiment_score, 1)
        self.assertEqual(moon.sentiment_score, 1)
