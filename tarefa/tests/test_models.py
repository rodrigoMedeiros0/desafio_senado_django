from django.test import TestCase
from tarefa.models import Tarefa

class TarefaModelTest(TestCase):
    def test_criacao_tarefa(self):
        tarefa = Tarefa.objects.create(
            nome_responsavel='João',
            titulo='Testando Tarefa',
            descricao='Descrição teste para tarefa.'
        )
        self.assertEqual(tarefa.nome_responsavel, 'João')
        self.assertEqual(tarefa.titulo, 'Testando Tarefa')
        self.assertEqual(tarefa.descricao, 'Descrição teste para tarefa.')
