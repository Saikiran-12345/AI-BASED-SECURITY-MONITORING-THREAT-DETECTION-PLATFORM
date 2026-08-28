from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Placeholder for risk views

class UserBehaviorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserBehavior.objects.all()
    serializer_class = UserBehaviorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['risk_level', 'user']
    ordering_fields = ['risk_score', 'last_updated']

class RiskAssessmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user']
    ordering_fields = ['assessed_at', 'score']
