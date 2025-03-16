from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class PrincipalView(QMainWindow):
    def __init__(self, parent=None):
        super(PrincipalView, self).__init__(parent)
        uic.loadUi("screens/frm_principal.ui", self)
        self.setWindowTitle("Principal")
        self.setGeometry(100, 100, 800, 600)
