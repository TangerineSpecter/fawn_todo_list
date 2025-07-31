from django.urls import path

from dashboard.views import DashboardView

urlpatterns = [
    path('overview', DashboardView.as_view(), name='dashboard')
]
