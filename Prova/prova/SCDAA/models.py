from ast import If
from django.db import models
from django.db.models import Sum
# Create your models here.

class Itens(models.Model):
    descricao = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.descricao

    class Meta:
        verbose_name_plural = "Itens"

class Entidades(models.Model):
    nome = models.TextField(max_length=100)
    bairro = models.TextField(max_length=100)
    cidade = models.TextField(max_length=100)
    estado = models.TextField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = "Entidades"

class Coletas(models.Model):
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Coletas"

    def getTotalDoacoes():
        queryset_list = []
        for entidade in Entidades.objects.all():
            queryset_list.append(Coletas.objects.filter(entidade=entidade).aggregate(quantidade_total=Sum('quantidade')))
            queryset_list[-1]['entidade'] = entidade

        return queryset_list
    
    def getSumDoacoes():
        total = Coletas.objects.aggregate(quantidade_total=Sum('quantidade'))

        return total

    def getSumItens():
        total = Coletas.objects.aggregate(quantidade_total=Sum('quantidade'))

        return total

    def getTotalItens():
        queryset_list = []
        total = Coletas.getSumItens()
        for item in Itens.objects.all():
            quantidade = Coletas.objects.filter(item=item).aggregate(quantidade_total=Sum('quantidade'))
            queryset_list.append(quantidade)
            queryset_list[-1]['item'] = item
            if quantidade['quantidade_total'] == None:
                queryset_list[-1]['porcentagem'] = 0
            else:
                queryset_list[-1]['porcentagem'] = '%.2f' % ((quantidade['quantidade_total'] / total['quantidade_total']) * 100)  + " %"

        return queryset_list
