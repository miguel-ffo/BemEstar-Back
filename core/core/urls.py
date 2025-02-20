from django.urls import path, re_path, include 
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

schema_view = get_schema_view(
    openapi.Info(
        title="BemEstar60+ API",
        default_version='v1',
        description="API para gerenciamento de usuários, treinos e saúde no BemEstar60+",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Inclua o app de autenticação
    path('auth/', include('authentication.urls'), name='Authentication'),
]