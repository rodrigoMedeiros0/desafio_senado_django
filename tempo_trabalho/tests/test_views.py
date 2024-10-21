from django.test import TestCase
from django.urls import reverse
from tempo_trabalho.models import RegistroTempo
from tarefa.models import Tarefa
from datetime import datetime
from django.utils import timezone

class RegistroTempoViewsTest(TestCase):
    
    def setUp(self):
        self.tarefa = Tarefa.objects.create(
            nome_responsavel="João da Silva",
            titulo="Tarefa de Teste",
            descricao="Descrição de teste"
        )
        self.registro = RegistroTempo.objects.create(
            tarefa=self.tarefa,
            horas_trabalhadas=2.5,
            descricao_trabalho="Descrição de teste para registro",
            data_registro=timezone.now()
        )
    
    def test_listar_registros_tempo_view(self):
        response = self.client.get(reverse('listar_registros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tempo_trabalho/home.html')
        self.assertContains(response, self.registro.descricao_trabalho)

    def test_detalhe_registro_tempo_view(self):
        response = self.client.get(reverse('detalhe_registro_tempo', args=[self.registro.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tempo_trabalho/detalhe_registro_tempo.html')
        self.assertContains(response, self.registro.descricao_trabalho)

    def test_salvar_registro_view(self):
        response = self.client.post(reverse('salvar_registro'), {
            'tarefa_id': self.tarefa.id,
            'horas_trabalhadas': '2:30',
            'descricao_trabalho': 'Registro de horas de teste'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(RegistroTempo.objects.count(), 2)  

