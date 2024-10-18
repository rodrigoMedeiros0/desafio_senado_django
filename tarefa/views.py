from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Tarefa


def listar_tarefa(request):
    tarefas = Tarefa.objects.all()

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
