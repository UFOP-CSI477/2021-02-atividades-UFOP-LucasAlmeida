from django.shortcuts import render
from django.views import generic
from SCDAA.models import Coletas

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def geral(request):
    return render(request, 'geral.html', context={'total_doacoes_dic':Coletas.getTotalDoacoes(), 'total_doacoes':Coletas.getSumDoacoes(), 'total_itens_dic': Coletas.getTotalItens, 'total_itens': Coletas.getSumItens()})
