
from django.db import models
from django.conf import settings

class RiskLevel(models.TextChoices):
    LOW = 'LOW', 'Low'
    MEDIUM = 'MEDIUM', 'Medium'
    HIGH = 'HIGH', 'High'
    CRITICAL = 'CRITICAL', 'Critical'

class UserBehavior(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='behavior_profile')
    
    login_frequency = models.FloatField(default=0.0) # logins per day
    failed_login_count = models.IntegerField(default=0)
    successful_login_count = models.IntegerField(default=0)
    activity_frequency = models.FloatField(default=0.0)
    unusual_event_count = models.IntegerField(default=0)
    
    risk_score = models.IntegerField(default=0) # 0 - 100
    risk_level = models.CharField(max_length=20, choices=RiskLevel.choices, default=RiskLevel.LOW)
    
    last_updated = models.DateTimeField(auto_now=True)
    
    def update_risk_level(self):
        if self.risk_score < 25:
            self.risk_level = RiskLevel.LOW
        elif self.risk_score < 50:
            self.risk_level = RiskLevel.MEDIUM
        elif self.risk_score < 75:
            self.risk_level = RiskLevel.HIGH
        else:
            self.risk_level = RiskLevel.CRITICAL
        self.save()

class RiskAssessment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='risk_assessments')
    score = models.IntegerField()
    factors = models.JSONField(default=dict)
    assessed_at = models.DateTimeField(auto_now_add=True)
