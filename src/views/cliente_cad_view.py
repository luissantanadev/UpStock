from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class ClienteCadView(QMainWindow):
    def __init__(self, parent=None):
        super(ClienteCadView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_cadastro_cliente.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Cadastro de  Cliente")
        self.setGeometry(100, 100, 800, 600)