import pandas as pd
from datetime import timedelta
from django.utils import timezone
from apps.events.models import SecurityEvent
from apps.risk.models import UserBehavior

class BehaviorAnalyzer:
    def __init__(self):
        pass
        
    def analyze_user(self, user):
        # Gather last 30 days of events
        thirty_days_ago = timezone.now() - timedelta(days=30)
        events = SecurityEvent.objects.filter(user=user, timestamp__gte=thirty_days_ago)
        
        if not events.exists():
            return None
            
        df = pd.DataFrame(list(events.values('event_type', 'timestamp', 'risk_score')))
        
        # Calculations
        login_events = df[df['event_type'] == 'LOGIN']
        failed_logins = df[df['event_type'] == 'FAILED_LOGIN']
        
        login_freq = len(login_events) / 30.0
        failed_count = len(failed_logins)
        avg_risk = df['risk_score'].mean()
        
        # Update behavior profile
        profile, created = UserBehavior.objects.get_or_create(user=user)
        profile.login_frequency = login_freq
        profile.failed_login_count = failed_count
        profile.activity_frequency = len(df) / 30.0
        
        # Calculate risk score based on behavior
        risk = (failed_count * 5) + (avg_risk * 0.5)
        profile.risk_score = min(int(risk), 100)
        profile.update_risk_level()
        profile.save()
        
        return profile
        
    def analyze_all(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        for u in User.objects.all():
            self.analyze_user(u)
