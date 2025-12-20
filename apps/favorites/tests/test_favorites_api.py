from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status

from apps.news.models import Article
from apps.favorites.models import Favorite

User = get_user_model()


class FavoriteAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.article = Article.objects.create(
            external_id=99999,  # 👈 obligatorio
            title="Test article",
            summary="Test summary",
            url="https://example.com",
            image_url="https://example.com/img.jpg",
            news_site="NASA",
            published_at=timezone.now(),
        )


        self.client.force_authenticate(user=self.user)

    def test_add_favorite(self):
        url = f"/api/articles/{self.article.id}/favorite/"

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Favorite.objects.count(), 1)
        self.assertEqual(Favorite.objects.first().article, self.article)

    def test_list_favorites(self):
        Favorite.objects.create(user=self.user, article=self.article)

        url = "/api/favorites/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.article.id)

    def test_favorites_requires_auth(self):
        self.client.force_authenticate(user=None)

        url = "/api/favorites/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
