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

        return queryset_list