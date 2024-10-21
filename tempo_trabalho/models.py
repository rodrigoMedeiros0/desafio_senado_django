from django.db import models
from tarefa.models import Tarefa


class RegistroTempo(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_registro = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    horas_trabalhadas = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    descricao_trabalho = models.TextField(blank=False, null=False)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='registros_tempo')

    def __str__(self):
        return f"{self.tarefa.titulo} - {self.horas_trabalhadas} horas"
