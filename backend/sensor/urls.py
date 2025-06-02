from django.urls import path
from .views import SensorDataView

urlpatterns = [
    path('upload/', SensorDataView.as_view()),
]
