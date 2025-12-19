from typing import List
import requests

from apps.news.models import Article


SPACEFLIGHT_API_URL = "https://api.spaceflightnewsapi.net/v4/articles/"


def fetch_articles(limit: int = 10) -> int:
    """
    Fetch articles related to NASA, filter forbidden titles,
    calculate sentiment_score and store them in DB.
    Returns number of created articles.
    """

    params = {
        "search": "NASA",
        "limit": limit,
    }

    response = requests.get(SPACEFLIGHT_API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    articles: List[dict] = data.get("results", [])

    created_count = 0

    for item in articles:
        title = item.get("title", "")

        if "SpaceX" in title or "Musk" in title:
            continue

        sentiment_score = 1 if ("Mars" in title or "Moon" in title) else 0

        article, created = Article.objects.get_or_create(
            external_id=item["id"],
            defaults={
                "title": title,
                "summary": item.get("summary", ""),
                "url": item.get("url", ""),
                "news_site": item.get("news_site", ""),
                "published_at": item.get("published_at"),
                "sentiment_score": sentiment_score,
            },
        )

        if created:
            created_count += 1

    return created_count
