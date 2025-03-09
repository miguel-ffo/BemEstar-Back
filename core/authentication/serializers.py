from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User = get_user_model()

# Registrar Personal

class PersonalRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['role'] = 'personal'  # Força o papel de personal
        user = User.objects.create_user(**validated_data)
        return user

# Registrar Aluno

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        personal = self.context['request'].user  # Obtém o personal autenticado
        if personal.role != 'personal':
            raise serializers.ValidationError("Apenas personais podem criar alunos.")
        
        validated_data['role'] = 'usuario'
        validated_data['personal'] = personal  # Relaciona o aluno ao personal
        user = User.objects.create_user(**validated_data)
        return user

# Login

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('username')  # Aqui, "username" é o email fornecido pelo usuário
        password = attrs.get('password')

        # Usa o modelo de usuário personalizado
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Email ou senha incorretos.")

        if not user.check_password(password):
            raise serializers.ValidationError("Email ou senha incorretos.")
        
        # Retorna o token de acesso e refresh
        return super().validate(attrs)

# Redefinir Senha

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        required=True, 
        write_only=True, 
        style={"input_type": "password"}
    )
    new_password = serializers.CharField(
        required=True, 
        write_only=True, 
        style={"input_type": "password"}
    )
