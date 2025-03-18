from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class EstoqueView(QMainWindow):
    def __init__(self, parent=None):
        super(EstoqueView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_estoque.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Estoque")
        self.setGeometry(100, 100, 800, 600)
    def mostrar_produto(self, produto):
        pass

    def listar_produtos(self, produtos):
        pass
