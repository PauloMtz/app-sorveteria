from django.contrib import admin

from myapp.models import Embalagem, TipoSabor, Sabor

# Register your models here.
admin.site.register(Embalagem)
admin.site.register(TipoSabor)
admin.site.register(Sabor)
