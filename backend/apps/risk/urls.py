from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'behavior', UserBehaviorViewSet, basename='behavior')
router.register(r'assessments', RiskAssessmentViewSet, basename='assessments')

urlpatterns = [
    path('', include(router.urls)),
]
