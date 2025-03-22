import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from src.views.login_view import LoginView
from src.controllers.usuario_controller import UsuarioController

app = QApplication([])  # Precisa ser instanciado para testes com PyQt5

class TestLogin(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste"""
        print("Iniciando teste...")
        self.login_view = LoginView()
        self.login_view.show()

    def tearDown(self):
        """Fecha a janela após cada teste"""
        print("Finalizando teste...")
        self.login_view.close()

    def test_campos_vazios(self):
        """Testa se aparece erro ao tentar logar com campos vazios"""
        print("Testando campos vazios...")
        QTest.mouseClick(self.login_view.btnlogin, Qt.LeftButton)
        self.assertTrue(QMessageBox.warning.called)  # Verifica se a mensagem de erro foi exibida

    def test_login_invalido(self):
        """Testa se um usuário inválido exibe mensagem de erro"""
        print("Testando login inválido...")
        self.login_view.lineuser.setText("usuario_inexistente")
        self.login_view.linekey.setText("senha_errada")
        QTest.mouseClick(self.login_view.btnlogin, Qt.LeftButton)

        self.assertTrue(QMessageBox.warning.called)  # Verifica se a mensagem de erro foi exibida

    def test_login_valido(self):
        """Testa se um usuário válido faz login corretamente"""
        print("Testando login válido...")
        # Simulamos um usuário válido
        UsuarioController.cadastrar("Teste", "usuario_teste", "senha_teste")

        self.login_view.lineuser.setText("usuario_teste")
        self.login_view.linekey.setText("senha_teste")
        QTest.mouseClick(self.login_view.btnlogin, Qt.LeftButton)

        self.assertTrue(self.login_view.principal_view.isVisible())

if __name__ == "__main__":
    unittest.main()
