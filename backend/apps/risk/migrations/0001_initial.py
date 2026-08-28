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
            name='RiskAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('factors', models.JSONField(default=dict)),
                ('assessed_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_assessments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBehavior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_frequency', models.FloatField(default=0.0)),
                ('failed_login_count', models.IntegerField(default=0)),
                ('successful_login_count', models.IntegerField(default=0)),
                ('activity_frequency', models.FloatField(default=0.0)),
                ('unusual_event_count', models.IntegerField(default=0)),
                ('risk_score', models.IntegerField(default=0)),
                ('risk_level', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('CRITICAL', 'Critical')], default='LOW', max_length=20)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='behavior_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
