from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Tarefa
from django.core.paginator import Paginator 
from .filters import filtrar_tarefas


def listar_tarefa(request):
    tarefas_list = Tarefa.objects.all().order_by('-data_criacao')
    tarefas_list = filtrar_tarefas(request, tarefas_list)
    
    paginator = Paginator(tarefas_list, 10)

    page_number = request.GET.get('page')
    tarefas = paginator.get_page(page_number)

    return render(request, 'tarefa/home.html', {'tarefas': tarefas})


def salvar_tarefa(request):
    if request.method == 'POST':
        nome_responsavel = request.POST.get('nome_responsavel')
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if nome_responsavel and titulo:  # Campos obrigatórios
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
