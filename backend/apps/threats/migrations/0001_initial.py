# Created by Django 6.1 on 2026-08-28 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SUSPICIOUS_LOGIN', 'Suspicious Login'), ('ACCOUNT_ABUSE', 'Account Abuse'), ('UNUSUAL_ACTIVITY', 'Unusual Activity'), ('EXCESSIVE_REQUESTS', 'Excessive Requests'), ('ABNORMAL_DATA_ACCESS', 'Abnormal Data Access'), ('SUSPICIOUS_SESSION', 'Suspicious Session'), ('OTHER', 'Other')], max_length=50)),
                ('severity', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('CRITICAL', 'Critical')], max_length=20)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('INVESTIGATING', 'Investigating'), ('RESOLVED', 'Resolved'), ('FALSE_POSITIVE', 'False Positive')], default='OPEN', max_length=20)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('events', models.ManyToManyField(blank=True, related_name='threats', to='events.securityevent')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threats', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
