from django.contrib import admin
from .models import Paciente
# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paciente, PacienteAdmin)