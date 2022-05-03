from pyexpat import model
from django.db import models

# Create your models here.

STATUS_COMANDA_CHOICES = [
    ('Aberta', 'Aberta'),
    ('Fechada', 'Fechada'),
    ('Paga', 'Paga')
]

class Mesa(models.Model):
    nome = models.TextField(max_length=20)


class Funcionario(models.Model):
    nome = models.TextField(max_length=56)

class Item(models.Model):
    nome = models.TextField(max_length=256)
    preco = models.IntegerField()


class Comanda(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item, verbose_name="Itens na comanda")
    total = models.IntegerField()
    status = models.CharField(choices=STATUS_COMANDA_CHOICES, max_length=20)

class Bar(models.Model):
    comandas = models.ManyToManyField(Comanda, verbose_name="Comandas")


