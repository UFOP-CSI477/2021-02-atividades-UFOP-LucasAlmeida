from django.contrib import admin
from django.shortcuts import redirect
from SCDAA.models import Entidades, Itens, Coletas

# Register your models here.
admin.site.site_header = "Administração do SCDAA"

class ItensAdmin(admin.ModelAdmin):
    model = Itens
    ordering = ('descricao',)
    list_display = ("descricao", "created_at","updated_at")

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/geral')

    def response_change(self, request, obj):
        return redirect('/geral')

class EntidadesAdmin(admin.ModelAdmin):
    model = Entidades
    ordering = ('nome',)
    list_display = ("nome", "created_at","updated_at")

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/geral')

    def response_change(self, request, obj):
        return redirect('/geral')

class ColetasAdmin(admin.ModelAdmin):
    model = Coletas
    list_display = ("item", "entidade","created_at","updated_at")

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/geral')

    def response_change(self, request, obj):
        return redirect('/geral')



admin.site.register(Entidades, EntidadesAdmin)
admin.site.register(Itens, ItensAdmin)
admin.site.register(Coletas, ColetasAdmin)

