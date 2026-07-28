from django.db import models
from django.contrib.auth.models import User

from .services import calcular_preco_total_pote, calcular_preco_total_sacola

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

# Monta o Pote       
class MontaPote(models.Model):
    embalagem = models.ForeignKey(Embalagem, 
        related_name='embalagem', on_delete=models.CASCADE, null=True)
    cobertura = models.ManyToManyField(Cobertura)
    quantidade = models.PositiveIntegerField(null=True)

    def preco_total(self):
        return calcular_preco_total_pote(self)

    def __str__(self):
        return f"ID: {self.id} / POTE: {self.embalagem.tipo} / Qtd: {self.quantidade} / {self.preco_total()}"

    class Meta:
        verbose_name = 'Montar Pote'
        verbose_name_plural = 'b. Montar Potes'

# Seleciona Sabores
class SelSabor(models.Model):
    pote = models.ForeignKey(MontaPote, related_name='pote', on_delete=models.CASCADE, null=True)
    sabor = models.ForeignKey(Sabor, related_name='sabor', on_delete=models.CASCADE, null=True)
    quantidade_bolas = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Sabor: {self.sabor.nome}, Quantidade de Bolas: {self.quantidade_bolas}"
    
    class Meta:
        verbose_name = 'Selecionar Sabor'
        verbose_name_plural = 'a. Selecionar Sabores'

# Sacolas de Itens (Carrinho)
class SacolaItens(models.Model):
    potes = models.ManyToManyField(MontaPote)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def preco_total(self):
        return calcular_preco_total_sacola(self)
  
    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'

    def __str__(self):
        return f"CARRINHO: {self.id} / {self.preco_total()}"

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'c. Carrinho'

# Registro do Pedido
class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, related_name='pedido_user', on_delete=models.PROTECT)
    itens_da_sacola = models.OneToOneField(SacolaItens, on_delete=models.CASCADE, null=True)    
    status = models.BooleanField()
    pago = models.BooleanField()

    # Endereço
    # Pagamento

    def __str__(self):
        return f"Pedido: {self.id} / {self.user} / (PAGO: {self.pago})"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'd. Pedido'