from django.contrib import admin

from myapp.models import Embalagem, MontaPote, Pedido, SacolaItens, SelSabor, TipoSabor, Sabor, Cobertura

# Register your models here.
admin.site.register(Embalagem)
admin.site.register(TipoSabor)
admin.site.register(Sabor)
admin.site.register(Cobertura)
#admin.site.register(MontaPote)
#admin.site.register(SelSabor)
#admin.site.register(SacolaItens)
#admin.site.register(Pedido)

class SelSaborInline(admin.TabularInline):
    model = SelSabor
    extra = 0

@admin.register(MontaPote)
class MontaPoteAdmin(admin.ModelAdmin):
    inlines = [
        SelSaborInline
    ] 

# Sacola de Itens 
class MontaPoteInline(admin.TabularInline):
    model = SacolaItens.potes.through
    extra = 0

class PedidoInline(admin.StackedInline):
    model = Pedido
    extra = 0

@admin.register(SacolaItens)
class SacolaItensAdmin(admin.ModelAdmin):
    fields = ('preco',)
    readonly_fields = ('preco',)
    inlines = [PedidoInline, MontaPoteInline]
