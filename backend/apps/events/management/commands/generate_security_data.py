from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from apps.events.models import SecurityEvent, Severity, EventType
from apps.threats.models import Threat, ThreatCategory, ThreatStatus
from apps.alerts.models import Alert, AlertStatus
from apps.incidents.models import Incident, IncidentStatus
import random
import datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Generates synthetic security data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data generation...')
        
        # Create users
        users = []
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            admin.role = 'ADMIN'
            admin.save()
            users.append(admin)
            
        for i in range(1, 21):
            username = f'user_{i}'
            if not User.objects.filter(username=username).exists():
                u = User.objects.create_user(username, f'{username}@example.com', 'password123')
                u.role = random.choice(['USER', 'USER', 'USER', 'SECURITY_ANALYST'])
                u.save()
                users.append(u)
        
        if not users:
            users = list(User.objects.all())

        self.stdout.write(f'Created/loaded {len(users)} users.')
        
        event_types = list(EventType.choices)
        severities = list(Severity.choices)
        
        # Create events
        events_to_create = []
        now = timezone.now()
        for i in range(1000):
            user = random.choice(users)
            dt = now - datetime.timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
            
            # Simulate a few anomalies
            if random.random() < 0.05:
                # Anomaly!
                e_type = EventType.FAILED_LOGIN
                sev = Severity.HIGH
                risk = random.randint(60, 95)
            else:
                e_type = random.choice([e[0] for e in event_types])
                sev = random.choice([Severity.LOW, Severity.MEDIUM])
                risk = random.randint(5, 40)
                
            e = SecurityEvent(
                user=user,
                event_type=e_type,
                description=f"Auto-created event: {e_type} by {user.username}",
                severity=sev,
                source=random.choice(['web', 'api', 'mobile', 'internal']),
                status='NEW',
                risk_score=risk,
                ip_address=f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                location=random.choice(['US-East', 'US-West', 'EU-Central', 'AP-South'])
            )
            e.timestamp = dt
            events_to_create.append(e)
            
        SecurityEvent.objects.bulk_create(events_to_create)
        
        # Bulk create doesn't trigger auto_now_add well when overridden sometimes, but let's fix dates
        # Wait, since bulk_create doesn't call save(), we might need to update timestamps manually.
        events = list(SecurityEvent.objects.all())
        for idx, e in enumerate(events):
            e.timestamp = now - datetime.timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
            
        SecurityEvent.objects.bulk_update(events, ['timestamp'])
        
        self.stdout.write(f'Created {len(events)} events.')

        # Create threats
        threats_to_create = []
        for i in range(50):
            t = Threat.objects.create(
                category=random.choice([c[0] for c in ThreatCategory.choices]),
                user=random.choice(users),
                severity=random.choice([Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL]),
                status=random.choice([s[0] for s in ThreatStatus.choices]),
                description=f"Detected suspicious activity pattern #{i}"
            )
            # Assign random events
            t.events.set(random.sample(events, k=random.randint(1, 5)))
            threats_to_create.append(t)

        self.stdout.write(f'Created 50 threats.')
        
        # Create alerts
        for i in range(80):
            Alert.objects.create(
                event=random.choice(events) if random.random() > 0.5 else None,
                threat=random.choice(threats_to_create) if random.random() > 0.5 else None,
                user=random.choice(users),
                severity=random.choice([Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL]),
                risk_score=random.randint(50, 100),
                message=f"Alert: Risk threshold exceeded.",
                status=random.choice([s[0] for s in AlertStatus.choices])
            )

        self.stdout.write(f'Created 80 alerts.')

        # Create incidents
        analysts = [u for u in users if u.role in ['ADMIN', 'SECURITY_ANALYST']]
        for i in range(15):
            incident = Incident.objects.create(
                title=f"Incident Investigation #{i}",
                description="Investigating a cluster of alerts and threats.",
                severity=random.choice([Severity.HIGH, Severity.CRITICAL]),
                status=random.choice([s[0] for s in IncidentStatus.choices]),
                assigned_to=random.choice(analysts) if analysts else None
            )
            incident.alerts.set(list(Alert.objects.order_by('?')[:random.randint(1, 3)]))
            incident.threats.set(list(Threat.objects.order_by('?')[:random.randint(1, 2)]))

        self.stdout.write(f'Created 15 incidents.')
        self.stdout.write(self.style.SUCCESS('Successfully created all synthetic data.'))
