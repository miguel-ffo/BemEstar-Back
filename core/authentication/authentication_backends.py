from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Usa o email como 'username'
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
