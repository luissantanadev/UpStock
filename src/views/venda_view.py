from PyQt5 import uic
from PyQt5.QtWidgets import QGroupBox
import os

class CaixaView(QGroupBox):
    def __init__(self, parent=None):
        super(CaixaView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_vendas.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Vendas")
        self.setGeometry(100, 100, 800, 600)
