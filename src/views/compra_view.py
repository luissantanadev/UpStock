from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class CompraView(QMainWindow):
   def __init__(self, parent=None):
      super(CompraView, self).__init__(parent)
      uic.loadUi("screens/frm_compra.ui", self)
      self.setWindowTitle("Compra")
      self.setGeometry(100, 100, 800, 600)
   
