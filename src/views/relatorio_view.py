from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class VendaView(QMainWindow):
    def __init__(self, parent=None):
        super(VendaView, self).__init__(parent)
        uic.loadUi("screens/f.ui", self)
        self.setWindowTitle("Venda")
        self.setGeometry(100, 100, 800, 600)