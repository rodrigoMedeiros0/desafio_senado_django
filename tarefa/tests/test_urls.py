from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tarefa.views import listar_tarefa, salvar_tarefa, detalhe_tarefa, salvar_registro_direto


class TarefaUrlsTest(SimpleTestCase):

    def test_listar_tarefas_url_resolves(self):
        url = reverse('listar_tarefas')
        self.assertEqual(resolve(url).func, listar_tarefa)

    def test_salvar_tarefa_url_resolves(self):
        url = reverse('salvar_tarefa')
        self.assertEqual(resolve(url).func, salvar_tarefa)

    def test_detalhe_tarefa_url_resolves(self):
        url = reverse('detalhe_tarefa', args=[1])
        self.assertEqual(resolve(url).func, detalhe_tarefa)

    def test_salvar_registro_direto_url_resolves(self):
        url = reverse('salvar_registro_direto')
        self.assertEqual(resolve(url).func, salvar_registro_direto)
