from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    USER = 'USER', 'User'
    SECURITY_ANALYST = 'SECURITY_ANALYST', 'Security Analyst'
    ADMIN = 'ADMIN', 'Admin'

class User(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.USER
    )
    
    department = models.CharField(max_length=100, blank=True, null=True)
    is_active_employee = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
