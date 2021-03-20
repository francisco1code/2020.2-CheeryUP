from django.db import models
from django.contrib.auth.models import AbstractUser

class Psicologo(AbstractUser):
    crp = models.CharField(max_length=11)
    bio = models.TextField(blank=True)