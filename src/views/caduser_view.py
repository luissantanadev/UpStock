from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import os
from controllers.usuario_controller import UsuarioController

class CadastroUsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Caminho correto do arquivo .ui
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_caduser.ui')
        uic.loadUi(ui_path, self)

        # Conectando botão a função de cadastro
        self.btnSalvar.clicked.connect(self.cadastrar_usuario)

    def cadastrar_usuario(self):
        nome = self.line_nome.text()
        usuario = self.line_usuario.text()
        senha = self.line_senha.text()

        if not nome or not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
            return

        resultado = UsuarioController.cadastrar(nome, usuario, senha)

        if resultado:
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.close()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar usuário. Tente novamente.")
