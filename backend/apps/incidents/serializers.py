from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.CharField(source='assigned_to.username', read_only=True)
    
    class Meta:
        model = Incident
        fields = '__all__'
