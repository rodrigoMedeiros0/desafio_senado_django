from django.test import TestCase
from tempo_trabalho.models import RegistroTempo
from tarefa.models import Tarefa

class RegistroTempoModelTest(TestCase):
    def setUp(self):
        self.tarefa = Tarefa.objects.create(
            nome_responsavel="João da Silva",
            titulo="Tarefa de Teste",
            descricao="Descrição de teste"
        )

    def test_criacao_registro_tempo(self):
        registro = RegistroTempo.objects.create(
            tarefa=self.tarefa,
            horas_trabalhadas=5.0,
            descricao_trabalho="Desenvolvimento de features."
        )
        self.assertEqual(registro.tarefa, self.tarefa)
        self.assertEqual(registro.horas_trabalhadas, 5.0)
        self.assertEqual(registro.descricao_trabalho, "Desenvolvimento de features.")
