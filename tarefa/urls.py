from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefa, name='listar_tarefas'),
    path('salvar/', views.salvar_tarefa, name='salvar_tarefa'),
    path('detalhe/<int:id>', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('salvar-registro-direto/', views.salvar_registro_direto, name='salvar_registro_direto'),
]
