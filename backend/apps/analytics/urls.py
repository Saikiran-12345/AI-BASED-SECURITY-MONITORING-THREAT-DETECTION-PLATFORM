from django.urls import path
from .views import run_anomaly_detection, get_dashboard_stats

urlpatterns = [
    path('detect-anomalies/', run_anomaly_detection, name='detect_anomalies'),
    path('dashboard-stats/', get_dashboard_stats, name='dashboard_stats'),
]
