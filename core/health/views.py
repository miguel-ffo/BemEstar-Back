from django.forms import ValidationError
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import WaterConsumeModel
from .serializers import AnamnesisSerializer, WaterConsumeSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class WaterConsumeView(generics.CreateAPIView):
    """Registra ou atualiza o controle hídrico de um usuário"""
    serializer_class = WaterConsumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Obtendo os dados da requisição (não precisamos mais de user_id)
        date = request.data.get("date")
        water_goal = request.data.get("water_goal")
        water_consumed = request.data.get("water_consumed", 0)  # Definindo valor padrão para evitar nulo

        # Verificar se os campos obrigatórios estão presentes
        if not date or water_goal is None:
            raise PermissionDenied("Os campos 'date' e 'water_goal' são obrigatórios.")

        # O `user` será obtido a partir do usuário autenticado na requisição
        user = request.user

        # **Correção na criação do registro**
        # Tente criar ou obter um registro de controle hídrico
        water_entry, created = WaterConsumeModel.objects.get_or_create(
            user=user, date=date,
            defaults={"water_goal": water_goal, "water_consumed": water_consumed}  # Definindo valores padrão
        )

        if not created:  # Se já existir, apenas atualiza os valores
            water_entry.water_goal = water_goal
            water_entry.water_consumed = water_consumed
            water_entry.save()

        # Calculando a quantidade restante de água a ser consumida
        remaining = max(0, water_entry.water_goal - water_entry.water_consumed)

        return Response({"message": "Controle hídrico atualizado com sucesso", "remaining": remaining})


class AnamnesisCreateView(generics.CreateAPIView):
    """Usuário registra sua própria ficha de anamnese"""
    serializer_class = AnamnesisSerializer
    permission_classes = [permissions.IsAuthenticated]  # Apenas usuários autenticados

    def perform_create(self, serializer):
        # Impede que o usuário crie mais de uma anamnese
        if hasattr(self.request.user, 'anamnesis'):
            raise ValidationError({"detail": "Você já possui uma ficha de anamnese registrada."})
        
        # Associa a anamnese ao usuário autenticado
        serializer.save(user=self.request.user)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DailyRecordModel, GlycemiaModel, BloodPressureModel
from .serializers import DailyRecordSerializer

class DailyRecordCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Extrair os dados de glicemia e pressão arterial
        glycemia_data = request.data.get('glycemia')
        blood_pressure_data = request.data.get('blood_pressure')
        date = request.data.get('date')

        if not glycemia_data or not blood_pressure_data or not date:
            return Response({"message": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        # Criar os registros de glicemia e pressão arterial
        glycemia = GlycemiaModel.objects.create(
            user=request.user,
            date=date,
            pre_workout=glycemia_data['pre_workout'],
            post_workout=glycemia_data['post_workout']
        )

        blood_pressure = BloodPressureModel.objects.create(
            user=request.user,
            date=date,
            pre_workout_systolic=blood_pressure_data['pre_workout_systolic'],
            pre_workout_diastolic=blood_pressure_data['pre_workout_diastolic'],
            post_workout_systolic=blood_pressure_data['post_workout_systolic'],
            post_workout_diastolic=blood_pressure_data['post_workout_diastolic']
        )

        # Criar o registro diário com as referências para glicemia e pressão arterial
        daily_record = DailyRecordModel.objects.create(
            user=request.user,
            date=date,
            glycemia=glycemia,
            blood_pressure=blood_pressure
        )

        # Retorna o serializer da resposta
        serializer = DailyRecordSerializer(daily_record)
        return Response({"message": "Registro diário criado com sucesso.", }, status=status.HTTP_201_CREATED)

