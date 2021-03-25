from django.db import models
from django.contrib.auth.models import User


class Psicologo(models.Model):
    GENERO = (
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('P', 'Prefiro não responder'),
        )
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    nCRP = models.CharField(max_length=200)
    bio = models.TextField(max_length=300)
    genero = models.CharField(default = 'M', max_length=1, choices=GENERO)

