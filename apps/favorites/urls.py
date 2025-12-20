from django.urls import path
from apps.favorites.views import FavoriteListAPIView

urlpatterns = [
    path("favorites/", FavoriteListAPIView.as_view()),
]
