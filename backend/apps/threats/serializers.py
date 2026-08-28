from rest_framework import serializers
from .models import Threat
from apps.events.serializers import SecurityEventSerializer

class ThreatSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Threat
        fields = '__all__'
