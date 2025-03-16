from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class PrincipalView(QMainWindow):
    def __init__(self, parent=None):
        super(PrincipalView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_principal.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("UpStock - Sistema ERP")
        self.setGeometry(100, 100, 800, 600)
