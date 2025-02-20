from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer  # Ajuste para o nome correto
from .models import User  # Ajuste conforme o nome do modelo

class RegisterView(APIView):
    @extend_schema(
        summary="Registro de Personal Trainer",
        description="Endpoint para cadastrar um novo personal trainer.",
        request=RegisterSerializer,
        responses={201: RegisterSerializer},
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
