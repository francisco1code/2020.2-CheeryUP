from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User


admin.site.register(User, auth_admin.UserAdmin)

#@admin.register(User)

#class UserAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'email')