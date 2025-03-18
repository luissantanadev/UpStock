from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class UsuarioView(QMainWindow):
    def __init__(self, parent=None):
        super(UsuarioView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_caduser.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Venda")
        self.setGeometry(100, 100, 800, 600)