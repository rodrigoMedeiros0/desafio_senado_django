from .models import RegistroTempo


def filtrar_registros_tempo(request, queryset):
    tarefa_id = request.GET.get('tarefa_id')
    tarefa_titulo = request.GET.get('tarefa_titulo')
    responsavel = request.GET.get('responsavel')
    data_inicio = request.GET.get('data_registro_inicio')
    data_fim = request.GET.get('data_registro_fim')
    horas_trabalhadas = request.GET.get('horas_trabalhadas')
    descricao = request.GET.get('descricao')

    if tarefa_id:
        queryset = queryset.filter(tarefa__id=tarefa_id)
    if tarefa_titulo:
        queryset = queryset.filter(tarefa__titulo__icontains=tarefa_titulo)
    if responsavel:
        queryset = queryset.filter(tarefa__nome_responsavel__icontains=responsavel)
    if data_inicio:
        queryset = queryset.filter(data_registro__gte=data_inicio)
    if data_fim:
        queryset = queryset.filter(data_registro__lte=data_fim)
    if horas_trabalhadas:
        queryset = queryset.filter(horas_trabalhadas=horas_trabalhadas)
    if descricao:
        queryset = queryset.filter(descricao_trabalho__icontains=descricao)

    return queryset
