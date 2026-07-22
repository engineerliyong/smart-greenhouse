from django.urls import path
from .views import SensorReadingListCreate

urlpatterns = [
    path("sensor/", SensorReadingListCreate.as_view(), name="sensor-list-create"),
]