from django.test import TestCase
from django.urls import reverse
from tarefa.models import Tarefa
from datetime import datetime
from django.utils import timezone
from datetime import datetime

class TarefaViewsTest(TestCase):
    def setUp(self):
        self.tarefa = Tarefa.objects.create(
            nome_responsavel="João da Silva",
            titulo="Tarefa de Teste",
            descricao="Descrição de teste"
        )

    def test_listar_tarefa_view(self):
        response = self.client.get(reverse('listar_tarefas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tarefa/home.html')
        self.assertContains(response, self.tarefa.titulo)

    def test_salvar_tarefa_view(self):
        response = self.client.post(reverse('salvar_tarefa'), {
            'nome_responsavel': 'Maria Souza',
            'titulo': 'Nova Tarefa',
            'descricao': 'Descrição para nova tarefa'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Tarefa.objects.count(), 2)  

    def test_detalhe_tarefa_view(self):
        response = self.client.get(reverse('detalhe_tarefa', args=[self.tarefa.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tarefa/detalhe_tarefa.html')
        self.assertContains(response, self.tarefa.titulo)


class TarefaFilterTests(TestCase):

    def setUp(self):
        Tarefa.objects.create(
            nome_responsavel="João", 
            titulo="Primeira Tarefa", 
            descricao="Tarefa de teste", 
            data_criacao=timezone.make_aware(datetime(2024, 10, 1))
        )
        Tarefa.objects.create(
            nome_responsavel="Maria", 
            titulo="Segunda Tarefa", 
            descricao="Outra tarefa", 
            data_criacao=timezone.make_aware(datetime(2024, 10, 2))
        )

    def test_filtrar_por_responsavel(self):
        response = self.client.get(reverse('listar_tarefas'), {'responsavel': 'João'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Primeira Tarefa")
        self.assertNotContains(response, "Segunda Tarefa")

    def test_filtrar_por_titulo(self):
        response = self.client.get(reverse('listar_tarefas'), {'titulo': 'Segunda Tarefa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Segunda Tarefa")
        self.assertNotContains(response, "Primeira Tarefa")

    def test_filtrar_por_descricao(self):
        response = self.client.get(reverse('listar_tarefas'), {'descricao': 'Outra tarefa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Segunda Tarefa")
        self.assertNotContains(response, "Primeira Tarefa")
