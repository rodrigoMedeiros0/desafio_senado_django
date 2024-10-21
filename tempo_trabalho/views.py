from django.shortcuts import render, get_object_or_404, redirect
from .models import RegistroTempo
from tarefa.models import Tarefa
from django.contrib import messages
import logging
from .filters import filtrar_registros_tempo
from django.http import JsonResponse
from django.core.paginator import Paginator


logger = logging.getLogger(__name__)


def listar_registros_tempo(request):
    registros_list = RegistroTempo.objects.all().order_by('data_registro')
    tarefas = Tarefa.objects.all()

    registros_list = filtrar_registros_tempo(request, registros_list)
    filtro_aplicado = False

    if request.GET.get('tarefa_id') or request.GET.get('responsavel') or request.GET.get('data_registro_inicio') or request.GET.get('data_registro_fim') or request.GET.get('descricao'):
        registros_list = filtrar_registros_tempo(request, registros_list)
        filtro_aplicado = True

    paginator = Paginator(registros_list, 10)
    page_number = request.GET.get('page')
    registros = paginator.get_page(page_number)

    total_registros = registros_list.count()

    if filtro_aplicado and not registros_list.exists():
        messages.warning(request, 'Nenhum registro de horas trabalhadas encontrado com os filtros aplicados.')
        return redirect('listar_registros')

    return render(request, 'tempo_trabalho/home.html', {
        'registros': registros,
        'tarefas': tarefas,
        'total_registros': total_registros,
        'filtro_aplicado': filtro_aplicado
    })


def detalhe_registro_tempo(request, id):
    registro = get_object_or_404(RegistroTempo, id=id)

    horas_formatadas = registro.horas_formatadas()

    return render(request, 'tempo_trabalho/detalhe_registro_tempo.html', {
        'registro': registro,
        'horas_formatadas': horas_formatadas
    })


def salvar_registro(request):
    if request.method == 'POST':
        tarefa_id = request.POST.get('tarefa_id')
        horas_trabalhadas = request.POST.get('horas_trabalhadas')
        descricao_trabalho = request.POST.get('descricao_trabalho')

        try:
            horas, minutos = horas_trabalhadas.split(':')
            horas_decimal = int(horas) + int(minutos) / 60

            tarefa = get_object_or_404(Tarefa, id=tarefa_id)
            registro = RegistroTempo(
                tarefa=tarefa,
                horas_trabalhadas=horas_decimal,
                descricao_trabalho=descricao_trabalho
            )
            registro.save()

            messages.success(request, 'O Histórico de horas trabalhadas foi salvo com sucesso!')
            return redirect('listar_registros')

        except ValueError:
            messages.error(request, 'Formato inválido para horas trabalhadas. Por favor, insira no formato hh:mm.')
            return redirect('listar_registros')

        except Tarefa.DoesNotExist:
            messages.error(request, 'A tarefa selecionada não existe. Por favor, tente novamente.')
            return redirect('listar_registros')

        except Exception as e:
            logger.error(f'Erro ao salvar o registro: {str(e)}')

            messages.error(request, 'Ocorreu um erro ao salvar o registro. Tente novamente mais tarde.')
            return redirect('listar_registros')


def buscar_tarefas(request):
    query = request.GET.get('q', '')
    tarefas = Tarefa.objects.filter(titulo__icontains=query).values('id', 'titulo')
    return JsonResponse(list(tarefas), safe=False)
