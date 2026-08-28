# Created by Django 6.1 on 2026-08-28 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('LOGIN', 'Login'), ('LOGOUT', 'Logout'), ('FAILED_LOGIN', 'Failed Login'), ('PASSWORD_CHANGE', 'Password Change'), ('PROFILE_CHANGE', 'Profile Change'), ('DATA_ACCESS', 'Data Access'), ('FILE_ACCESS', 'File Access'), ('SETTINGS_CHANGE', 'Settings Change'), ('SUSPICIOUS_ACTIVITY', 'Suspicious Activity'), ('ACCOUNT_LOCK', 'Account Lock'), ('UNUSUAL_REQUEST', 'Unusual Request'), ('OTHER', 'Other')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('severity', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('CRITICAL', 'Critical')], default='LOW', max_length=20)),
                ('source', models.CharField(max_length=100)),
                ('status', models.CharField(default='NEW', max_length=50)),
                ('risk_score', models.IntegerField(default=0)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('device_info', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='security_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
