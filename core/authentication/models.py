from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('personal', 'Personal'),
        ('usuario', 'Usuário'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    personal = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="alunos",
        limit_choices_to={'role': 'personal'}
    )

    email = models.EmailField(unique=True)  # Garantir que o email seja único
    
    USERNAME_FIELD = 'email'  # Agora o email será usado para autenticação
    REQUIRED_FIELDS = ['username']  # Usado para criação de superusuário

    def __str__(self):
        return self.email  # Mostra o email como representação do usuário
# Mostra o email ao invés do username