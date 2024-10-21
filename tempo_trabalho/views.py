from django.shortcuts import render, get_object_or_404
from .models import RegistroTempo

def listar_registros_tempo(request):
    registros = RegistroTempo.objects.all().order_by('data_registro')
    return render(request, 'tempo_trabalho/home.html', {'registros': registros})

def detalhe_registro_tempo(request, id):
    registro = get_object_or_404(RegistroTempo, id=id)
    return render(request, 'tempo_trabalho/detalhe_registro_tempo.html', {'registro': registro})

