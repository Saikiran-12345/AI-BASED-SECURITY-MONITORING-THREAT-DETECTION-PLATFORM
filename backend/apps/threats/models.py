
from django.db import models
from django.conf import settings
from apps.events.models import SecurityEvent, Severity

class ThreatCategory(models.TextChoices):
    SUSPICIOUS_LOGIN = 'SUSPICIOUS_LOGIN', 'Suspicious Login'
    ACCOUNT_ABUSE = 'ACCOUNT_ABUSE', 'Account Abuse'
    UNUSUAL_ACTIVITY = 'UNUSUAL_ACTIVITY', 'Unusual Activity'
    EXCESSIVE_REQUESTS = 'EXCESSIVE_REQUESTS', 'Excessive Requests'
    ABNORMAL_DATA_ACCESS = 'ABNORMAL_DATA_ACCESS', 'Abnormal Data Access'
    SUSPICIOUS_SESSION = 'SUSPICIOUS_SESSION', 'Suspicious Session'
    OTHER = 'OTHER', 'Other'

class ThreatStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    INVESTIGATING = 'INVESTIGATING', 'Investigating'
    RESOLVED = 'RESOLVED', 'Resolved'
    FALSE_POSITIVE = 'FALSE_POSITIVE', 'False Positive'

class Threat(models.Model):
    category = models.CharField(max_length=50, choices=ThreatCategory.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='threats', null=True, blank=True)
    events = models.ManyToManyField(SecurityEvent, related_name='threats', blank=True)
    severity = models.CharField(max_length=20, choices=Severity.choices)
    status = models.CharField(max_length=20, choices=ThreatStatus.choices, default=ThreatStatus.OPEN)
    
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.category} - {self.severity} ({self.status})"
