from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    article = models.ForeignKey(
        "news.Article",
        on_delete=models.CASCADE,
        related_name="favorited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "article")

    def __str__(self):
        return f"{self.user} -> {self.article}"
