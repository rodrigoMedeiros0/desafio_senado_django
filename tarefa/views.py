from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Tarefa
from django.core.paginator import Paginator 
from .filters import filtrar_tarefas
from tempo_trabalho.models import RegistroTempo
from django.http import HttpResponseRedirect
from django.urls import reverse


def listar_tarefa(request):
    tarefas_list = Tarefa.objects.all().order_by('-data_criacao')
    tarefas_list = filtrar_tarefas(request, tarefas_list)
    filtro_aplicado = False

    if request.GET.get('data_inicio') or request.GET.get('data_final') or request.GET.get('responsavel') or request.GET.get('titulo') or request.GET.get('descricao'):
        tarefas_list = filtrar_tarefas(request, tarefas_list)
        filtro_aplicado = True

    paginator = Paginator(tarefas_list, 10)
    page_number = request.GET.get('page')
    tarefas = paginator.get_page(page_number)

    total_tarefas = tarefas_list.count()

    if filtro_aplicado and not tarefas_list.exists():
        filtro_aplicado = True
        messages.warning(request, 'Nenhuma tarefa encontrada com os filtros aplicados.')
        return HttpResponseRedirect(reverse('listar_tarefas'))

    return render(request, 'tarefa/home.html', {'tarefas': tarefas, 'total_tarefas': total_tarefas})


def salvar_tarefa(request):
    if request.method == 'POST':
        nome_responsavel = request.POST.get('nome_responsavel')
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if nome_responsavel and titulo and descricao:
            nova_tarefa = Tarefa(
                nome_responsavel=nome_responsavel,
                titulo=titulo,
                descricao=descricao
            )
            nova_tarefa.save()

            messages.success(request, 'Tarefa salva com sucesso!')
            return redirect('listar_tarefas')
        else:

            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return render(request, 'tarefa/listar_tarefas.html', {
                'error': 'Por favor, preencha os campos obrigatórios.'
            })

    return redirect('listar_tarefas')


def detalhe_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    registros = RegistroTempo.objects.filter(tarefa=tarefa).order_by('data_registro') 
    return render(request, 'tarefa/detalhe_tarefa.html', {
        'tarefa': tarefa,
        'registros': registros,  
    })

def salvar_registro_direto(request):
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

            messages.success(request, 'O registro de horas foi adicionado com sucesso!')
            return redirect('detalhe_tarefa', id=tarefa_id)

        except ValueError:
            messages.error(request, 'Formato inválido para horas trabalhadas. Insira no formato hh:mm.')
            return redirect('detalhe_tarefa', id=tarefa_id)

        except Tarefa.DoesNotExist:
            messages.error(request, 'A tarefa selecionada não existe.')
            return redirect('detalhe_tarefa', id=tarefa_id)

        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao salvar o registro. Tente novamente mais tarde.')
            return redirect('detalhe_tarefa', id=tarefa_id)

