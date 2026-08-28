from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Alert
        fields = '__all__'
