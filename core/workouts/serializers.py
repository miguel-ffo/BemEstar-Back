from rest_framework import serializers
from .models import Workout

# Registrar Treino

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'date', 'status', 'description']  # Incluindo a descrição
        read_only_fields = ['user']  # O usuário será definido automaticamente


# Listar Treino

class WorkoutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['date', 'status', 'description']  # Removendo o campo 'id' e mantendo a descrição
 # Aqui você pode incluir apenas os campos que quer exibir
