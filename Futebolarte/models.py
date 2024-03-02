from django.db import models
from cadastros_comuns.models import *

DIVISAO_CHOICES = (
    ('A', 'Serie A'),
    ('B', 'Serie B'),
    ('C', 'Serie C'),
    ('D', 'Serie D'),
    ('E', 'Serie E'),
)


class Clube(models.Model):
    nome = models.CharField(max_length=130, blank=False, null=False)
    fundacao = models.PositiveIntegerField('Fundação', help_text="Ano de fundação do clube")
    divisao = models.CharField(max_length=64, choices=DIVISAO_CHOICES, default='S', blank=False, null=False)
    escudo = models.ImageField(upload_to='escudos', null=True, blank=True)

    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'

    def __srt__(self):
          return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=130, blank=False, null=False)
    numero_camisa = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='jogadores', null=True)

    clube = models.ForeignKey(Clube, on_delete=models.CASCADE, null=False)
    
    class Meta:
       verbose_name = 'Jogador'
       verbose_name_plural = 'Jogadores'

    def __srt__(self):
          return self.nome
