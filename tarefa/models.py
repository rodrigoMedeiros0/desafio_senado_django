from django.db import models


class Tarefa(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    nome_responsavel = models.CharField(max_length=255, blank=False, null=False)
    titulo = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.titulo
