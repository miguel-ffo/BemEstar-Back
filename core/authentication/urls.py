from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ChangePasswordView, LoginView, RegisterPersonalView, RegisterUserView, ListAlunosView

urlpatterns = [
    path('personal/register/', RegisterPersonalView.as_view(), name='register_personal'),
    path('users/register/', RegisterUserView.as_view(), name='register_user'),
    path('personal/users/', ListAlunosView.as_view({'get': 'list'}), name='list_alunos'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
