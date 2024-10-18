from django.shortcuts import render
from .models import Tarefa


def listar_tarefa(request):
    tarefas = Tarefa.objects.all()

    return render(request, 'tarefa/home.html', {'tarefas': tarefas})
