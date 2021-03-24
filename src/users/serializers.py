
from rest_framework import serializers
from .models import Psicologo

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psicologo
        fields = ('user', 'name', 'email', 'nCRP', 'bio', 'genero')