from django.db import models

class Article(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.URLField()
    source = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    sentiment_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
