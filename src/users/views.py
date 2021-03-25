from django.shortcuts import render
from rest_framework import viewsets
from .models import Psicologo
from .serializers import UsersSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class PsicologoViewSet(viewsets.ModelViewSet):
    queryset = Psicologo.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (permissions.AllowAny,)
    
