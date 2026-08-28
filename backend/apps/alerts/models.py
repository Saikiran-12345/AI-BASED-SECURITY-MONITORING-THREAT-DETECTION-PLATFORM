
from django.db import models
from django.conf import settings
from apps.events.models import SecurityEvent, Severity
from apps.threats.models import Threat

class AlertStatus(models.TextChoices):
    NEW = 'NEW', 'New'
    ACKNOWLEDGED = 'ACKNOWLEDGED', 'Acknowledged'
    INVESTIGATING = 'INVESTIGATING', 'Investigating'
    RESOLVED = 'RESOLVED', 'Resolved'
    DISMISSED = 'DISMISSED', 'Dismissed'

class Alert(models.Model):
    event = models.ForeignKey(SecurityEvent, on_delete=models.CASCADE, null=True, blank=True, related_name='alerts')
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE, null=True, blank=True, related_name='alerts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='alerts')
    
    severity = models.CharField(max_length=20, choices=Severity.choices)
    risk_score = models.IntegerField(default=0)
    message = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=AlertStatus.choices, default=AlertStatus.NEW)
    
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Alert: {self.message} ({self.status})"
