from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ml.utilities.ml_engine import MLEngine
from apps.events.models import SecurityEvent
from apps.threats.models import Threat
from apps.alerts.models import Alert
import datetime
from django.utils import timezone

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def run_anomaly_detection(request):
    engine = MLEngine()
    anomaly_ids = engine.detect_anomalies()
    return Response({
        'status': 'success',
        'anomalies_found': len(anomaly_ids),
        'event_ids': anomaly_ids
    })

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_dashboard_stats(request):
    total_events = SecurityEvent.objects.count()
    total_threats = Threat.objects.count()
    total_alerts = Alert.objects.count()
    
    # recent events (last 7 days)
    seven_days = timezone.now() - datetime.timedelta(days=7)
    recent_events = SecurityEvent.objects.filter(timestamp__gte=seven_days).count()
    
    return Response({
        'total_events': total_events,
        'total_threats': total_threats,
        'total_alerts': total_alerts,
        'recent_events': recent_events,
    })
