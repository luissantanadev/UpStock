from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton
import os as os_module
from controllers.usuario_controller import UsuarioController
from views.principal_view import PrincipalView

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        # caminho do arquivo .ui
        ui_path = os_module.path.join(os_module.path.dirname(__file__), '../views/screens/frm_login.ui')
        uic.loadUi(ui_path, self)

        # Configurando o campo de senha para ocultar o texto
        self.linekey = self.findChild(QLineEdit, 'linekey')
        self.linekey.setEchoMode(QLineEdit.Password)

        # Encontrando outros elementos da interface
        self.lineuser = self.findChild(QLineEdit, 'lineuser')
        self.btnlogin = self.findChild(QPushButton, 'btnlogin')
        

    def connect_signals(self):
        # Conectando o botão ao método realizar_login
        self.btnlogin.clicked.connect(self.realizar_login)

        # Conectando o Enter no lineuser para avançar para o linekey
        self.lineuser.returnPressed.connect(lambda: self.linekey.setFocus())

        # Conectando o Enter no linekey para realizar o login
        self.linekey.returnPressed.connect(self.realizar_login)

    def realizar_login(self):
        usuario = self.lineuser.text()
        senha = self.linekey.text()
        
        if not self.validar_campos(usuario, senha):
            return

        if self.verificar_credenciais is not None or not False:
            return self.abrir_principal()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

    def validar_campos(self, usuario, senha):
        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return False
        return True

    def verificar_credenciais(self, usuario, senha):
        # Verifica se o usuário e senha estão corretos
        return UsuarioController.verificar_login(usuario, senha)

    def abrir_principal(self):
        self.principal_view = PrincipalView()
        self.principal_view.show()
        self.close()