from django.contrib import admin
from django.urls import path, include
from paciente.views import PacienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))

]