from django.db import models
from django.conf import settings
from django.utils import timezone

class Workout(models.Model):
    STATUS_CHOICES = (
        ('done', 'Treino Concluído'),
        ('missed', 'Faltou'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="workouts"
    )
    date = models.DateField(default=timezone.now)  # Permite escolher a data do treino
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.email} - {self.date} - {self.get_status_display()}"
