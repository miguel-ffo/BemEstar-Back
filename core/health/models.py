from django.utils import timezone
from django.conf import settings
from django.db import models


# Modelo para o registro de consumo de água

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

# Modelo para a ficha de anamnese

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


# Modelo para glicemia

class GlycemiaModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    pre_workout = models.IntegerField()
    post_workout = models.IntegerField()

    def __str__(self):
        return f"Glicemia de {self.user} - {self.date}"


# Modelo para pressão arterial

class BloodPressureModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    pre_workout_systolic = models.IntegerField()
    pre_workout_diastolic = models.IntegerField()
    post_workout_systolic = models.IntegerField()
    post_workout_diastolic = models.IntegerField()

    def __str__(self):
        return f"Pressão arterial de {self.user} - {self.date}"
    

# Modelo para o registro diário de saúde

class DailyRecordModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    
    # Relacionamentos com os modelos de glicemia e pressão arterial
    glycemia = models.ForeignKey(GlycemiaModel, on_delete=models.CASCADE, null=True, blank=True)
    blood_pressure = models.ForeignKey(BloodPressureModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Registro diário de saúde de {self.user} - {self.date}"
