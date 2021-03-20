from django.contrib import admin
from django.contrib.auth import admin as auth_admin


from .forms import UserChangeForm, UserCreationForm
from .models import Psicologo

@admin.register(Psicologo)
class PsicologoAdmin(auth_admin.UserAdmin):
    form =  UserChangeForm
    add_form = UserCreationForm
    model = Psicologo
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos do psicologo",  {"fields" : ("crp", 'bio',)}),

    )
