from rest_framework import serializers


class StationForecastRealDataSerializer(serializers.Serializer):
    ty_code = serializers.CharField()
    gp_id = serializers.IntegerField()
    station_code = serializers.CharField()
    forecast_index = serializers.IntegerField()
    forecast_dt = serializers.DateTimeField()
    surge = serializers.FloatField()
