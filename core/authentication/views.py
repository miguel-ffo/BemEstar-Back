from rest_framework import generics, permissions, viewsets, status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth import authenticate, login

from .models import User
from .serializers import ChangePasswordSerializer, PersonalRegisterSerializer, UserRegisterSerializer,LoginSerializer, ChangePasswordSerializer

# Registro de Personal
class RegisterPersonalView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PersonalRegisterSerializer
    permission_classes = [permissions.AllowAny]  # Qualquer um pode se registrar
    

# Registro de Usuário

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]  # Só personal autenticado pode cadastrar

# Listar Usuários

class ListAlunosView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role != 'personal':
            return User.objects.none()  # Retorna vazio se não for personal
        return user.alunos.all()  # Retorna apenas os alunos do personal autenticado

# Login

class LoginView(APIView):
    permission_classes = [AllowAny]  # Permite qualquer um fazer login

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response("Login com sucesso."),
            400: openapi.Response("Preencha o email e senha."),
            401: openapi.Response("Credenciais inválidas."),
        },
    )
    
    def post(self, request):
        data = request.data
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return Response({"error": "Por favor, preencha o email e a senha."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login com sucesso."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

# Trocar Senha

class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body=ChangePasswordSerializer,
        responses={200: openapi.Response("Senha alterada com sucesso")},
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Lógica de alteração de senha
            return Response({"message": "Senha alterada com sucesso"}, status=200)
        return Response(serializer.errors, status=400)
