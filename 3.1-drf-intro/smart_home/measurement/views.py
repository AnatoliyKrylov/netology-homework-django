from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSensorSerializer


class SensorView(ListCreateAPIView):
    """Создать датчик(POST) и получить список всех датчиков(GET)"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    """Изменить датчик(PATCH) и получить информацию по конкретному датчику(GET)"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    """Добавить измерение по датчику (POST)"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSensorSerializer
