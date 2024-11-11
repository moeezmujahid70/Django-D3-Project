from django.urls import path
from charts.api_views import ChartDataAPI

urlpatterns = [
    path('chart-data/', ChartDataAPI.as_view(), name='chart-data'),
    
]