from django.contrib import admin
from bar.models import Bar, Comanda, ComandaItens, Mesa, Item, Funcionario
# Register your models here.
admin.site.site_header = "Administração do Pede Bem"

class ComandaItensAdmin(admin.ModelAdmin):
    list_display = ("item", "comanda")
    list_filter = ('comanda__mesa','comanda__status')

    def get_form(self, request, obj=None, **kwargs):
        form = super(ComandaItensAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['comanda'].queryset = ComandaItens.comanda.get_queryset().exclude(status='Paga')
        return form

class ComandaAdmin(admin.ModelAdmin):
    list_display = ("mesa", "status")
    list_filter = ('status',)
admin.site.register(Comanda, ComandaAdmin)
admin.site.register(Item)
admin.site.register(ComandaItens, ComandaItensAdmin)

