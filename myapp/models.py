from django.db import models

# Create your models here.
class Embalagem(models.Model):
    tipo = models.CharField(max_length=50)
    capacidade_maxima_bolas = models.PositiveIntegerField()
    ativo = models.BooleanField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def preco_formatado(self):
        return f'R$ {self.preco:.2f}' # Formata por ex R$ 23.30
    
    def __str__(self):
        return f'Embalagem de {self.tipo} - PREÇO: R$ {self.preco:.2f}'

    class Meta:
        verbose_name = 'Embalagem'
        verbose_name_plural = 'Embalagens'

