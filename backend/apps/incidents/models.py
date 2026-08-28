
from django.db import models
from django.conf import settings
from apps.events.models import Severity
from apps.alerts.models import Alert
from apps.threats.models import Threat

class IncidentStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    INVESTIGATING = 'INVESTIGATING', 'Investigating'
    CONTAINED = 'CONTAINED', 'Contained'
    RESOLVED = 'RESOLVED', 'Resolved'
    CLOSED = 'CLOSED', 'Closed'

class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    severity = models.CharField(max_length=20, choices=Severity.choices)
    status = models.CharField(max_length=20, choices=IncidentStatus.choices, default=IncidentStatus.OPEN)
    
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_incidents')
    
    alerts = models.ManyToManyField(Alert, related_name='incidents', blank=True)
    threats = models.ManyToManyField(Threat, related_name='incidents', blank=True)
    
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
