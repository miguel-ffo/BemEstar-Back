from django.urls import path
from .views import AnamnesisCreateView, WaterConsumeView

app_name = 'health'

urlpatterns = [
    path('water-intake/', WaterConsumeView.as_view(), name='water-intake'),
    path('anamnesis/', AnamnesisCreateView.as_view(), name='anamnesis'),
]