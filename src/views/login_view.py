from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton
import os
import sys
from controllers.usuario_controller import UsuarioController
import mysql.connector
import mysql.connector.errors
from PyQt5.QtWidgets import QApplication



class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        # caminho do arquivo .ui
        ui_path = os.path.join(os.path.dirname(__file__), '../views/screens/frm_login.ui')
        uic.loadUi(ui_path, self)

        # Configurando o campo de senha para ocultar o texto
        self.linekey = self.findChild(QLineEdit, 'linekey')
        self.linekey.setEchoMode(QLineEdit.Password)

        # Conectando os botões aos métodos
        self.btnlogin = self.findChild(QPushButton, 'btnlogin')
        self.btnlogin.clicked.connect(self.realizar_login)

        self.lineuser = self.findChild(QLineEdit, 'lineuser')

    def realizar_login(self):
        login = self.lineuser.text()
        senha = self.linekey.text()
        if not self.validar_campos(login, senha):
            return
        test_controller = UsuarioController.verificar_login(login, senha)
        if test_controller:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso.")
            self.abrir_principal()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")


    def validar_campos(self, login, senha):
        if not login or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return False
        return True

    def abrir_principal(self):
        from views.principal_view import PrincipalView
        self.principal_view = PrincipalView()
        self.principal_view.show()
        self.close()  # Fecha a tela de login