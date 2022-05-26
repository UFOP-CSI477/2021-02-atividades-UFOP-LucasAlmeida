from django.shortcuts import render, get_object_or_404
from django.views import generic

from bar.models import Comanda
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def comandas(request):
    return render(request, 'comandas.html', ComandaListView.get_queryset() )

class ComandaListView(generic.ListView):
    model = Comanda
    context_object_name = 'comanda_list'
    queryset = model.objects.exclude(status='Paga')
    template_name = "../templates/comandas.html"

class ComandaDetailView(generic.DetailView):
    model = Comanda

    def comanda_detail_view(request, primary_key):
        comanda = get_object_or_404(Comanda, pk=primary_key)
        return render(request, "../templates/bar/comanda_detail.html", context={'comanda': comanda})
