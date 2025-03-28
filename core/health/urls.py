from django.urls import path
from .views import AnamnesisCreateView, DailyRecordCreateView, DailyRecordGetView, WaterConsumeView

app_name = 'health'

urlpatterns = [
    path('water-intake/', WaterConsumeView.as_view(), name='water-intake'),
    path('anamnesis/', AnamnesisCreateView.as_view(), name='anamnesis'),
    path('daily-record/', DailyRecordCreateView.as_view(), name='daily-record-create'),
    path('daily-record-view/', DailyRecordGetView.as_view(), name='daily-record-get'),

]