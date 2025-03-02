from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Workout
from .serializers import WorkoutSerializer, WorkoutListSerializer


#Registrar Treino

class RegisterWorkoutView(generics.CreateAPIView):
    """Usuário registra a própria frequência de treino"""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]  # Apenas usuários autenticados podem registrar

    def perform_create(self, serializer):
        # Impede que o personal registre treinos
        if self.request.user.role == 'personal':
            raise PermissionDenied("Personal não pode registrar treinos.")
        # Salva o treino com o usuário autenticado
        serializer.save(user=self.request.user)

# Listar Treinos

class ListWorkoutView(generics.ListAPIView):
    """Exibe os treinos de um usuário (aluno) para um personal ou os treinos do próprio usuário."""
    serializer_class = WorkoutListSerializer
    permission_classes = [permissions.IsAuthenticated]  # Apenas usuários autenticados podem acessar

    
    def get_queryset(self):
        user = self.request.user
        aluno_id = self.request.query_params.get('id')  # Obtém o ID do aluno via query param

        if not aluno_id:
            raise PermissionDenied("O ID do aluno deve ser fornecido para personal.")

        if user.role == 'personal':
            # Se o usuário for personal, ele pode visualizar os treinos do aluno com o ID fornecido
            return Workout.objects.filter(user__id=aluno_id)
        else:
            # Se não for personal, o usuário só vê seus próprios treinos
            return Workout.objects.filter(user=user)
