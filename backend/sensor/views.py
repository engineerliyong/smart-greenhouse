from rest_framework import generics
from .models import SensorReading
from .serializers import SensorReadingSerializer

class SensorReadingListCreate(generics.ListCreateAPIView):
    queryset = SensorReading.objects.all().order_by("-created_at")
    serializer_class = SensorReadingSerializer