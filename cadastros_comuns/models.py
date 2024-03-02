from django.db import models

# Create your models here.
class Pais(models.Model):
    nome = models.CharField(max_length=130)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
    
    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=130)
    uf = models.CharField(max_length=2, null=True, blank=False)
    
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=130)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nome} - {self.estado.uf} - {self.estado.pais.nome}'