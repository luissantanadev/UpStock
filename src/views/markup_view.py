from controllers.produto_controller import MarkupController
from models.produto import Markup
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class MarkupView(QMainWindow):  # Corrigir a herança para QMainWindow
    def __init__(self, parent=None):
        super(MarkupView, self).__init__(parent)  # Agora o super() está correto
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_markup.ui')
        uic.loadUi(ui_path, self)