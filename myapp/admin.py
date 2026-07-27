from django.contrib import admin

from myapp.models import Embalagem, MontaPote, Pedido, Pedido, SacolaItens, SelSabor, TipoSabor, Sabor, Cobertura

# Register your models here.
admin.site.register(Embalagem)
admin.site.register(TipoSabor)
admin.site.register(Sabor)
admin.site.register(Cobertura)
admin.site.register(MontaPote)
admin.site.register(SelSabor)
admin.site.register(SacolaItens)
admin.site.register(Pedido)
