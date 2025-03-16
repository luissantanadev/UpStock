# tests/test_cliente.py

import unittest
from src.controllers.cliente_controller import ClienteController
from src.models.cliente import Cliente

class TestCliente(unittest.TestCase):
    def setUp(self):
        """Configuração inicial: Criar uma instância do ClienteController"""
        self.controller = ClienteController()

    def test_cadastrar_cliente(self):
        """Testa o cadastro de um novo cliente"""
        resultado = self.controller.cadastrar_cliente(
            cnpjcpf="12345678000195",
            descricao="Empresa Teste LTDA",
            cep="12345678",
            endereco="Rua Exemplo, 123",
            bairro="Centro",
            cidade="São Paulo",
            uf="SP",
            telefone="1122334455",
            celular="11998765432",
            email="teste@email.com"
        )
        self.assertIn("cadastrado com sucesso", resultado)

    def test_buscar_cliente_por_id(self):
        """Testa se um cliente pode ser buscado corretamente"""
        cliente = Cliente.get_by_id(1)  # Testa se há um cliente com ID 1
        if cliente:
            resultado = self.controller.buscar_cliente_por_id(cliente.idcliente)
            self.assertEqual(resultado["idcliente"], cliente.idcliente)
            self.assertEqual(resultado["cnpjcpf"], cliente.cnpjcpf)
        else:
            self.skipTest("Nenhum cliente com ID 1 no banco para testar.")

    def test_atualizar_cliente(self):
        """Testa a atualização de um cliente"""
        cliente = Cliente.get_by_id(1)
        if cliente:
            resultado = self.controller.atualizar_cliente(
                idcliente=cliente.idcliente,
                cnpjcpf="98765432000112",
                descricao="Empresa Atualizada",
                cep="87654321",
                endereco="Rua Nova, 456",
                bairro="Bairro Novo",
                cidade="Rio de Janeiro",
                uf="RJ",
                telefone="2133445566",
                celular="21987654321",
                email="novo@email.com"
            )
            self.assertIn("atualizado com sucesso", resultado)
        else:
            self.skipTest("Nenhum cliente com ID 1 no banco para testar atualização.")

    def test_excluir_cliente(self):
        """Testa a remoção de um cliente"""
        cliente = Cliente.get_by_id(1)
        if cliente:
            resultado = self.controller.excluir_cliente(cliente.idcliente)
            self.assertIn("excluído com sucesso", resultado)
        else:
            self.skipTest("Nenhum cliente com ID 1 para testar exclusão.")

if __name__ == "__main__":
    unittest.main()
