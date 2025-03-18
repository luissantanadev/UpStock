from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class CaixaView(QMainWindow):
    def __init__(self, parent=None):
        super(CaixaView, self).__init__(parent)
        uic.loadUi("screens/frm_venda.ui", self)
        self.setWindowTitle("Venda")
        self.setGeometry(100, 100, 800, 600)
