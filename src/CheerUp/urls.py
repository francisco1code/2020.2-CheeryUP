from django.contrib import admin
from django.urls import path, include
# from paciente.views import PacienteViewSet
from rest_framework import routers

from paciente.urls import router as paciente_router
from users.urls import router as psicologo_router

router = routers.DefaultRouter()
router.registry.extend(paciente_router.registry)
router.registry.extend(psicologo_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api/register/', include('users.urls')),
]
