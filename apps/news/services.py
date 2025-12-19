import requests
from datetime import datetime
from django.conf import settings
from .models import Article

SPACEFLIGHT_API_URL = "https://api.spaceflightnewsapi.net/v4/articles/"

def fetch_articles(limit=10):
    response = requests.get(SPACEFLIGHT_API_URL, params={"limit": limit})
    response.raise_for_status()

    data = response.json()["results"]
    articles = []

    for item in data:
        article, created = Article.objects.update_or_create(
            external_id=item["id"],
            defaults={
                "title": item.get("title", ""),
                "summary": item.get("summary", ""),
                "url": item.get("url", ""),
                "image_url": item.get("image_url", ""),
                "news_site": item.get("news_site", ""),
                "published_at": item.get("published_at"),
                "sentiment_score": 0, #Falta aplicar logica
            },
        )
        articles.append(article)

    return articles
