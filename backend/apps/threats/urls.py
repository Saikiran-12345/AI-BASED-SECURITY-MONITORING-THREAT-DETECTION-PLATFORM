from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', ThreatViewSet, basename='threats')

urlpatterns = [
    path('', include(router.urls)),
]
