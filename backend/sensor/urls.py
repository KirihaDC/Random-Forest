from django.urls import path
from .views import SensorDataView
from . import views

urlpatterns = [
    path('upload/', SensorDataView.as_view()),
    path('api/upload/', views.sensor_data_upload, name='sensor_data_upload'),
]
