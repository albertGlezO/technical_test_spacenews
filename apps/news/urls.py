from django.urls import path
from apps.news.views import MonthlyReportAPIView
from apps.favorites.views import ArticleFavoriteAPIView, FavoriteListAPIView

urlpatterns = [
    path("reports/monthly/", MonthlyReportAPIView.as_view()),
    path("favorites/", FavoriteListAPIView.as_view()),
    path("articles/<int:id>/favorite/", ArticleFavoriteAPIView.as_view()),

]
