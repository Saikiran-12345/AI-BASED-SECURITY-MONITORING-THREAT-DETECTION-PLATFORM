
from django.db import models
from django.conf import settings

class Severity(models.TextChoices):
    LOW = 'LOW', 'Low'
    MEDIUM = 'MEDIUM', 'Medium'
    HIGH = 'HIGH', 'High'
    CRITICAL = 'CRITICAL', 'Critical'

class EventType(models.TextChoices):
    LOGIN = 'LOGIN', 'Login'
    LOGOUT = 'LOGOUT', 'Logout'
    FAILED_LOGIN = 'FAILED_LOGIN', 'Failed Login'
    PASSWORD_CHANGE = 'PASSWORD_CHANGE', 'Password Change'
    PROFILE_CHANGE = 'PROFILE_CHANGE', 'Profile Change'
    DATA_ACCESS = 'DATA_ACCESS', 'Data Access'
    FILE_ACCESS = 'FILE_ACCESS', 'File Access'
    SETTINGS_CHANGE = 'SETTINGS_CHANGE', 'Settings Change'
    SUSPICIOUS_ACTIVITY = 'SUSPICIOUS_ACTIVITY', 'Suspicious Activity'
    ACCOUNT_LOCK = 'ACCOUNT_LOCK', 'Account Lock'
    UNUSUAL_REQUEST = 'UNUSUAL_REQUEST', 'Unusual Request'
    OTHER = 'OTHER', 'Other'

class SecurityEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='security_events')
    event_type = models.CharField(max_length=50, choices=EventType.choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=Severity.choices, default=Severity.LOW)
    source = models.CharField(max_length=100) # e.g. web, api, mobile
    status = models.CharField(max_length=50, default='NEW')
    risk_score = models.IntegerField(default=0)
    
    # Synthetic Demo Values
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.event_type} - {self.user} - {self.timestamp}"
