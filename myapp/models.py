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
        verbose_name_plural = '1. Embalagens'

# Tradicional / Premium / Sorbet / Açai
class TipoSabor(models.Model):
    tipo = models.CharField(max_length=100)
    ativo = models.BooleanField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'
    
    def __str__(self):
        return f'{self.tipo} - PREÇO: R$ {self.preco:.2f}'

    class Meta:
        verbose_name = 'Tipo de sabor'
        verbose_name_plural = '2. Tipos de sabor'

# Lista de Sabores (relacionamento com TipoSabor)
class Sabor(models.Model):
    nome = models.CharField(max_length=50) # Ninho
    tipo = models.ForeignKey(TipoSabor, 
        related_name='tipo_sabor', 
        on_delete=models.CASCADE)
    ativo = models.BooleanField() 
    
    def __str__(self):
        return f'{self.nome} - PREÇO: R$ {self.tipo.preco:.2f}'

    class Meta:
        verbose_name = 'Sabor'
        verbose_name_plural = '3. Sabores'

# Coberturas Disponiveis (Adicionais)
class Cobertura(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'
    
    def __str__(self):
        return f'{self.nome} - PREÇO: R$ {self.preco:.2f}'
    
    class Meta:
        verbose_name = 'Cobertura'
        verbose_name_plural = '4. Coberturas'
