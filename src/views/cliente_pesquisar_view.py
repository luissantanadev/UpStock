from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class ClientePesquisaView(QMainWindow):
    def __init__(self, parent=None):
        super(ClientePesquisaView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_pesquisa_clientes.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Pesquisa Cliente")
        self.setGeometry(100, 100, 800, 600)