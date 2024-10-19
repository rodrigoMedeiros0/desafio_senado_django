from .models import Tarefa
from datetime import datetime, timedelta


def filtrar_tarefas(request, queryset):
    data_inicio = request.GET.get('data_inicio')
    data_final = request.GET.get('data_final')
    responsavel = request.GET.get('responsavel')
    titulo = request.GET.get('titulo')
    descricao = request.GET.get('descricao')

    if data_inicio:
        queryset = queryset.filter(data_criacao__gte=data_inicio)
    if data_final:
        data_final_obj = datetime.strptime(data_final, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)
        queryset = queryset.filter(data_criacao__lte=data_final_obj)
    if responsavel:
        queryset = queryset.filter(nome_responsavel__icontains=responsavel)
    if titulo:
        queryset = queryset.filter(titulo__icontains=titulo)
    if descricao:
        queryset = queryset.filter(descricao__icontains=descricao)

    return queryset

