import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt 
from src.views.login_view import LoginView
from src.controllers.usuario_controller import UsuarioController
from src.models.usuario import Usuario


app = QApplication([]) # Cria uma instância do QApplication para os testes

class TestLoginView(unittest.TestCase):
    def setUp(self):
        # Configura o ambiente de teste
        self.login_view = LoginView()
        self.login_view.show()

    def tearDown(self):
        # Fecha a tela de login após os testes
        self.login_view.close()

    def test_login_success(self):
        # Simula a entrada de dados corretos
        self.login_view.lineuser.setText("adm")
        self.login_view.linekey.setText("adm")
        
        # Simula o clique no botão de login
        QTest.mouseClick(self.login_view.btnlogin, Qt.LeftButton)
        
        # Verifica se a tela principal foi aberta (aqui você pode verificar se a tela principal está visível ou não)
        # self.assertTrue(self.login_view.principal_view.isVisible())

    def test_login_invalido(self):
        # Simula a entrada de dados incorretos
        self.login_view.lineuser.setText("usuario_incorreto")
        self.login_view.linekey.setText("senha_incorreta")
        
        # Simula o clique no botão de login
        QTest.mouseClick(self.login_view.btnlogin, Qt.LeftButton)
        
        # Verifica se a mensagem de erro foi exibida (aqui você pode verificar se a mensagem de erro está visível ou não)
        # self.assertTrue(QMessageBox.warning.called)  # Exemplo, ajuste conforme necessário

if __name__ == "__main__":
    unittest.main()
#     # Executa os testes