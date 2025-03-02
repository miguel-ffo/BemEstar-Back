from django.urls import path
from .views import RegisterWorkoutView, ListWorkoutView

urlpatterns = [
    path('register/', RegisterWorkoutView.as_view(), name='register_workout'),
    path('list/', ListWorkoutView.as_view(), name='list_workouts'),  # Listagem dos treinos

    ]
