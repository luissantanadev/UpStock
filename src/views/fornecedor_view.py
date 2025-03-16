from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class FornecedorView(QMainWindow):
    def __init__(self, parent=None):
        super(FornecedorView, self).__init__(parent)
        uic.loadUi("screens/frm_pesquisa_fornecedor.ui", self)
        self.setWindowTitle("Fornecedor")
        self.setGeometry(100, 100, 800, 600)
    