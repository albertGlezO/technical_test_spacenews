from rest_framework import serializers

class MonthlyReportSerializer(serializers.Serializer):
    month = serializers.SerializerMethodField()
    total = serializers.IntegerField()
    top_site = serializers.CharField()

    def get_month(self, obj):
        return obj["month"].strftime("%Y-%m")
