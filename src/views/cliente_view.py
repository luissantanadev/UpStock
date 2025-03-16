from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class ClienteView(QMainWindow):
    def __init__(self, parent=None):
        super(ClienteView, self).__init__(parent)
        uic.loadUi("screens/cliente.ui", self)
        self.setWindowTitle("Cliente")
        self.setGeometry(100, 100, 800, 600)