from django.db import models

# Create your models here.

class Servico(models.Model):
    nome=models.CharField(max_length=100, verbose_name='Nome do serviço')
    link=models.CharField(max_length=150, verbose_name='Link')
    destaque=models.BooleanField(default=False, verbose_name='Destacar')
