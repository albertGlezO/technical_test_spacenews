from django.core.management.base import BaseCommand
from apps.news.services import fetch_articles

class Command(BaseCommand):
    help = "Sync latest space news articles"

    def add_arguments(self, parser):
        parser.add_argument(
            "--limit",
            type=int,
            default=10,
            help="Number of articles to fetch",
        )

    def handle(self, *args, **options):
        limit = options["limit"]
        articles = fetch_articles(limit=limit)

        self.stdout.write(
            self.style.SUCCESS(f"✔ {len(articles)} articles synced successfully")
        )
