from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.accounts.urls')),
    path('api/events/', include('apps.events.urls')),
    path('api/threats/', include('apps.threats.urls')),
    path('api/alerts/', include('apps.alerts.urls')),
    path('api/incidents/', include('apps.incidents.urls')),
    path('api/risk/', include('apps.risk.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/audit/', include('apps.audit.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
]

