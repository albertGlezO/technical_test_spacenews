from django.db.models import Count, OuterRef, Subquery
from django.db.models.functions import TruncMonth
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.news.models import Article
from apps.news.serializers import MonthlyReportSerializer


class MonthlyReportAPIView(APIView):
    authentication_classes = []  # público
    permission_classes = []

    def get(self, request):
        queryset = (
            Article.objects
            .annotate(month=TruncMonth("published_at"))
            .values("month")
            .annotate(
                total=Count("id"),
                top_site=Subquery(
                    Article.objects
                    .annotate(month=TruncMonth("published_at"))
                    .values("month", "news_site")
                    .annotate(site_total=Count("id"))
                    .filter(month=OuterRef("month"))
                    .order_by("-site_total")
                    .values("news_site")[:1]
                )
            )
            .order_by("month")
        )

        serializer = MonthlyReportSerializer(queryset, many=True)
        return Response(serializer.data)
