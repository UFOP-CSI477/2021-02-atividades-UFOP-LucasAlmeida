from django.contrib import admin
from django.shortcuts import redirect
from SCDAA.models import Entidades, Itens, Coletas

# Register your models here.
admin.site.site_header = "Administração do SCDAA"

admin.site.register(Entidades)
admin.site.register(Itens)
admin.site.register(Coletas)

