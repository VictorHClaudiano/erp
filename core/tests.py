from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Cliente

class TestExcluirCliente(TestCase):

    def setUp(self):
        # Criando um cliente inicial para testar a exclusão
        self.cliente = Cliente.objects.create(
            nome='João', email='joao@example.com', telefone='111111111'
        )

    def test_excluir_cliente_com_id_valido(self):
        # URL para excluir o cliente, com o ID do cliente
        url = reverse('excluir_cliente', args=[self.cliente.id])

        # Enviando a requisição para excluir o cliente
        response = self.client.get(url)

        # Verificando se o cliente foi excluído do banco de dados
        with self.assertRaises(Cliente.DoesNotExist):
            Cliente.objects.get(id=self.cliente.id)

        # Verificando se o redirecionamento para a lista de clientes ocorreu
        self.assertRedirects(response, reverse('listar_clientes'))

        # Verificando se a mensagem de sucesso foi exibida
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Cliente excluído com sucesso!')

    def test_excluir_cliente_com_id_invalido(self):
        # URL com um ID que não existe
        url = reverse('excluir_cliente', args=[999])  # ID que não existe

        # Enviando a requisição para excluir o cliente
        response = self.client.get(url)

        # Verificando se a resposta não foi um redirecionamento (ainda está na página de listagem)
        self.assertRedirects(response, reverse('listar_clientes'))

        # Verificando se a mensagem de erro foi exibida
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Cliente não encontrado!')
