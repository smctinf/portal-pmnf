from django.db import models

# Create your models here.

class Servico(models.Model):
    secretaria=models.CharField(max_length=100, verbose_name='Secretaria')
    nome=models.CharField(max_length=100, verbose_name='Nome do serviço')
    link=models.CharField(max_length=150, verbose_name='Link')
    descricao=models.CharField(max_length=150, blank=True,verbose_name='Breve descrição')
    destaque=models.BooleanField(default=False, verbose_name='Destacar')

    def __str__(self):
        return '%s' % (self.nome)

