import unittest
import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

# Ajustando o caminho do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils')))
from src.models.usuario import Usuario
from src.controllers.usuario_controller import UsuarioController
from src.utils.database import Database
"""
from src.views.login_view import LoginView

from src.views.principal_view import PrincipalView

# Verifica se já existe um QApplication rodando
if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()

class TestLogin(unittest.TestCase):
    def setUp(self):
        #Configuração inicial para cada teste
        print("Iniciando teste...")
        self.login_view = LoginView()
        self.login_view.show()

        # Criar usuário de teste se não existir
        usuario_teste = Usuario("Administrador", "adm", "adm")
        usuario_teste.salvar()

    def tearDown(self):
        #Fecha a janela após cada teste
        print("Finalizando teste...")
        self.login_view.close()

    def test_login_valido(self):
        #Testa se um usuário válido faz login corretamente
        print("Testando login válido...")
        self.login_view.lineuser.setText("adm")
        self.login_view.linekey.setText("adm")
        QTest.mouseClick(self.login_view.btnlogin, Qt.LeftButton)
        controler = UsuarioController.verificar_login("adm", "adm")
        print(f"Resultado do login: {controler}")
        QTest.qWait(500)  # Aguarda um tempo para a interface responder

        # Verifica se a tela principal foi criada corretamente antes de acessá-la
        if hasattr(self.login_view, 'principal_view'):
            self.assertTrue(self.login_view.principal_view.isVisible())
        else:
            self.fail("Erro: Tela principal não foi aberta após login bem-sucedido.")

if __name__ == "__main__":
    unittest.main()
"""
login = "adm"
senha = "adm"
models = Usuario.verificar(login, senha)
print(f"Resultado do login: {models}")

controller = UsuarioController.verificar_login(login, senha)
print(f"Resultado do login: {controller}")