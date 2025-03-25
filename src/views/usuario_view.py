from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton
import os
from controllers.usuario_controller import UsuarioController

class UsuarioView(QMainWindow):
    def __init__(self, parent=None):
        super(UsuarioView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_caduser.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Cadastro de Usuário")
        # Configurando a janela
        self.setGeometry(100, 100, 800, 600)

        # elementos da interface
        self.lineNome = self.findChild(QLineEdit, 'lineNome')
        self.lineUser = self.findChild(QLineEdit, 'lineUser')
        self.btnSalvar = self.findChild(QPushButton, 'btnSalvar')
        self.btnSalvar.clicked.connect(self.salvar_usuario)
        

        # Configurando o campo de senha para ocultar o texto
        self.lineKey = self.findChild(QLineEdit, 'lineKey')
        self.lineKey.setEchoMode(QLineEdit.Password)

    def salvar_usuario(self):
        nome = self.lineNome.text()
        login = self.lineUser.text()
        senha = self.lineKey.text()

        if not nome or not login or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        if UsuarioController.cadastrar(nome, login, senha):
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso.")
            
        else:
            QMessageBox.warning(self, "Erro", "Falha ao cadastrar o usuário.")
