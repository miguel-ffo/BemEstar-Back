from django.utils import timezone
from django.conf import settings
from django.db import models

class WaterConsumeModel(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="water_consume"  # Mudando o related_name para algo mais apropriado
    )
    
    date = models.DateField(default=timezone.now) 
    water_goal = models.IntegerField()
    water_consumed = models.IntegerField()  # Alterado para seguir o contrato

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.email} - {self.date} - {self.water_goal} - {self.water_consumed}"  

class AnamnesisModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="anamnesis"
    )
    weight = models.FloatField()
    height = models.FloatField()
    medical_conditions = models.JSONField(default=list)  # Lista de condições médicas
    medications = models.JSONField(default=list)  # Lista de medicamentos
    exercise_frequency = models.CharField(max_length=255)
    goals = models.TextField()

    def __str__(self):
        return f"Anamnese de {self.user.get_full_name() or self.user.email}"
