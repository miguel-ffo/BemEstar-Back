from rest_framework import generics, permissions
from .models import User
from .serializers import ChangePasswordSerializer, PersonalRegisterSerializer, UserRegisterSerializer

class RegisterPersonalView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PersonalRegisterSerializer
    permission_classes = [permissions.AllowAny]  # Qualquer um pode se registrar


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]  # Só personal autenticado pode cadastrar

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserRegisterSerializer

class ListAlunosView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role != 'personal':
            return User.objects.none()  # Retorna vazio se não for personal
        return user.alunos.all()  # Retorna apenas os alunos do personal autenticado


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutCreateView(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]


from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

@api_view(['POST'])
def login_view(request):
    if request.method == "POST":
        try:
            # Carrega os dados do corpo da requisição
            data = request.data

            # Obtém o e-mail e a senha
            email = data.get("email")
            password = data.get("password")

            # Verifica se os dados foram fornecidos corretamente
            if not email or not password:
                return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Tenta autenticar o usuário
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]  # Garante que o usuário esteja autenticado

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            
            # Checa se a senha antiga fornecida é a correta
            if not request.user.check_password(old_password):
                return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Atualiza a senha
            request.user.set_password(new_password)
            request.user.save()
            
            # Opcional: Reautentica o usuário após a mudança de senha
            # (Isso é útil se você deseja que o usuário seja desconectado após trocar a senha)
            authenticate(request, username=request.user.username, password=new_password)

            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
