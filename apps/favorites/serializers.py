from rest_framework import serializers
from apps.favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(source="article.title", read_only=True)
    article_summary = serializers.CharField(source="article.summary", read_only=True)
    article_id = serializers.IntegerField(source="article.id", read_only=True)

    class Meta:
        model = Favorite
        fields = [
            "id",
            "article_id",
            "article_title",
            "article_summary",
            "created_at",
        ]
