from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.news.models import Article
from apps.favorites.models import Favorite

from apps.favorites.serializers import FavoriteSerializer

class ArticleFavoriteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        article = get_object_or_404(Article, id=id)

        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            article=article
        )

        if not created:
            return Response(
                {"detail": "Article already marked as favorite"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"detail": "Article added to favorites"},
            status=status.HTTP_201_CREATED
        )

class FavoriteListAPIView(APIView):
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)