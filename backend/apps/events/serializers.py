from rest_framework import serializers
from .models import SecurityEvent

class SecurityEventSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = SecurityEvent
        fields = '__all__'
