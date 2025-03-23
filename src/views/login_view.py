from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton
import os
from controllers.usuario_controller import UsuarioController

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        # caminho do arquivo .ui
        ui_path = os.path.join(os.path.dirname(__file__), '../views/screens/frm_login.ui')
        uic.loadUi(ui_path, self)

        # Configurando o campo de senha para ocultar o texto
        self.linekey = self.findChild(QLineEdit, 'linekey')
        self.linekey.setEchoMode(QLineEdit.Password)

        # Encontrando outros elementos da interface
        self.btnlogin = self.findChild(QPushButton, 'btnlogin')
        self.lineuser = self.findChild(QLineEdit, 'lineuser')

    def connect_signals(self):
        # Conectando os botões aos métodos
        self.btnlogin.clicked.connect(self.realizar_login)

    def realizar_login(self):
        usuario = self.lineuser.text()
        senha = self.linekey.text()

        if not self.validar_campos(usuario, senha):
            return

        if self.verificar_credenciais(usuario, senha):
            self.abrir_principal()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

    def validar_campos(self, usuario, senha):
        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return False
        return True

    def verificar_credenciais(self, usuario, senha):
        test_controller = UsuarioController.verificar_login(usuario, senha)
        print(f"Verificando credenciais: {test_controller}")
        return test_controller

    def abrir_principal(self):
        print("Abrindo tela principal...")  # Depuração
        from src.views.principal_view import PrincipalView
        self.principal_view = PrincipalView()
        self.principal_view.show()
        self.close()