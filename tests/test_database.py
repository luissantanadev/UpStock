import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils')))
import mysql.connector
import mysql.connector.errors
from src.utils.database import Database
from src.models.usuario import Usuario
from src.controllers.usuario_controller import UsuarioController

class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.database = Database()
        self.connection = self.database.connection

    def tearDown(self):
        """Finalização após cada teste."""
        if self.connection:
            self.database.close()

    def test_connection_established(self):
        """Teste para verificar se a conexão com o banco de dados foi estabelecida."""
        self.assertIsNotNone(self.connection, "A conexão com o banco de dados não foi estabelecida.")

    def test_usuario_verificar_login(self):
        """Teste para verificar a autenticação de um usuário."""
        login = "adm"
        senha = "adm"
        resultado = UsuarioController.verificar_login(login, senha)
        self.assertIsNotNone(resultado, "Falha na autenticação do usuário.")
        self.assertTrue(Usuario.verificar(login, senha), "As credenciais do usuário são inválidas.")

    def test_invalid_login(self):
        """Teste para verificar autenticação com credenciais inválidas."""
        login = "invalido"
        senha = "invalido"
        resultado = UsuarioController.verificar_login(login, senha)
        self.assertIsNone(resultado, "A autenticação deveria falhar para credenciais inválidas.")

if __name__ == "__main__":
    unittest.main()