import unittest
from src.controllers.usuario_controller import UsuarioController
from src.models.usuario import Usuario

class TestUsuarioController(unittest.TestCase):
    def setUp(self):
        # Configurações iniciais para os testes, se necessário
        pass

    def test_cadastrar(self):
        # Teste para o método cadastrar
        nome = "Teste"
        login = "teste"
        senha = "senha123"
        resultado = UsuarioController.cadastrar(nome, login, senha)
        self.assertTrue(resultado)

    def test_verificar_login(self):
        # Teste para o método verificar_login
        login = "teste"
        senha = "senha123"
        resultado = UsuarioController.verificar_login(login, senha)
        self.assertTrue(resultado)

    def test_atualizar_senha(self):
        # Teste para o método atualizar_senha
        login = "teste"
        nova_senha = "nova_senha123"
        resultado = UsuarioController.atualizar_senha(login, nova_senha)
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()