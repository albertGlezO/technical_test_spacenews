from django.urls import path
from apps.news.views import MonthlyReportAPIView

urlpatterns = [
    path("reports/monthly/", MonthlyReportAPIView.as_view()),
]
