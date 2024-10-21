from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tempo_trabalho.views import listar_registros_tempo, detalhe_registro_tempo, salvar_registro, buscar_tarefas


class RegistroTempoURLsTest(SimpleTestCase):

    def test_listar_registros_url_resolves(self):
        url = reverse('listar_registros')
        self.assertEqual(resolve(url).func, listar_registros_tempo)

    def test_detalhe_registro_url_resolves(self):
        url = reverse('detalhe_registro_tempo', args=[1])
        self.assertEqual(resolve(url).func, detalhe_registro_tempo)

    def test_salvar_registro_url_resolves(self):
        url = reverse('salvar_registro')
        self.assertEqual(resolve(url).func, salvar_registro)

    def test_buscar_tarefas_url_resolves(self):
        url = reverse('buscar_tarefas')
        self.assertEqual(resolve(url).func, buscar_tarefas)
