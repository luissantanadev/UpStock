from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton
import os
from controllers.usuario_controller import UsuarioController
from views.principal_view import PrincipalView

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        # caminho do arquivo .ui
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_login.ui')
        uic.loadUi(ui_path, self)

        # Configurando o campo de senha para ocultar o texto
        self.linekey = self.findChild(QLineEdit, 'linekey')
        self.linekey.setEchoMode(QLineEdit.Password)

        # Conectando os botões aos métodos
        self.btnlogin = self.findChild(QPushButton, 'btnlogin')
        self.btnlogin.clicked.connect(self.realizar_login)

        self.lineuser = self.findChild(QLineEdit, 'lineuser')

    def realizar_login(self):
        # Obtendo os valores dos campos de entrada
        login = self.lineuser.text()
        senha = self.linekey.text()

        # Verificando se o usuário e senha estão corretos
        if not self.validar_campos(login, senha):
            return
        if UsuarioController.verificar_login(login, senha) == True:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso.")
            self.abrir_principal()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")
            return

    def validar_campos(self, login, senha):
        if not login or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return False
        return True

    def abrir_principal(self):
        # Fecha a tela de login e abre a tela principal
        self.close() # Fecha a tela de login
        print("Login realizado com sucesso.")
        self.principal_view = PrincipalView()
        self.principal_view.show()
