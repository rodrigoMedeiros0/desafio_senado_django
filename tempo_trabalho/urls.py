from django.urls import path
from . import views


urlpatterns = [
    path('registros/', views.listar_registros_tempo, name='listar_registros'),
    path('registro/<int:id>', views.detalhe_registro_tempo, name='detalhe_registro_tempo'),
    path('salvar/', views.salvar_registro, name='salvar_registro'),
    path('buscar-tarefas/', views.buscar_tarefas, name='buscar_tarefas'),
]
