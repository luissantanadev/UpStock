from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
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
        self.linekey.setEchoMode(QLineEdit.Password)

        # Conectando os botões aos métodos
        self.btnlogin.clicked.connect(self.realizar_login)

    def realizar_login(self):
        # Obtendo os valores dos campos de entrada
        login = self.lineuser.text()
        senha = self.linekey.text()

        # Verificando se o usuário e senha estão corretos
        if not login or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return
        if UsuarioController.verificar_login(login, senha):
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso.")
            self.abrir_principal()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")
            return
    def abrir_principal(self):
        # Fecha a tela de login e abre a tela principal
        self.principal_view = PrincipalView()
        self.principal_view.show()
        self.close() # Fecha a tela de login