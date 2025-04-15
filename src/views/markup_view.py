from controllers.produto_controller import MarkupController
from models.produto import Markup
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QDoubleValidator
import os
from views.produto_view import ProdutoView
class MarkupView(QMainWindow):  # Corrigir a herança para QMainWindow
    def __init__(self, parent=None):
        super(MarkupView, self).__init__(parent)  # Agora o super() está correto
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_markup.ui')
        uic.loadUi(ui_path, self)
        
        # elementos da interface
        self.linedf =  self.findChild(QLineEdit, 'linedf')
        self.linedv =  self.findChild(QLineEdit, 'linedv')  
        self.linelp =  self.findChild(QLineEdit, 'linelp')
        self.btncalcular =  self.findChild(QPushButton, 'btncalcular')
        self.btnenviar =  self.findChild(QPushButton, 'btnenviar')
        self.linemarkup =  self.findChild(QLineEdit, 'linemarkup')
        
        # Configurar validadores para aceitar apenas números
        double_validator = QDoubleValidator(0.0, 999999.99, 2, self)  # Limite de 2 casas decimais
        self.linedf.setValidator(double_validator)
        self.linedv.setValidator(double_validator)
        self.linelp.setValidator(double_validator)

        # Conectando os botões aos métodos
        self.btncalcular.clicked.connect(self.calcular_markup)
        self.btnenviar.clicked.connect(self.enviar_markup)
    
    def calcular_markup(self):
        # Substituir vírgulas por pontos antes de converter para float
        dv1 = float(self.linedv.text().replace(',', '.'))
        df1 = float(self.linedf.text().replace(',', '.'))
        lp1 = float(self.linelp.text().replace(',', '.'))
        markup = Markup(0)  # Passar um valor inicial ao construtor
        markup_value = markup.calcular_preco_venda(dv1, df1, lp1)
        self.linemarkup.setText(str(markup_value))  # Exibir o valor calculado
    def enviar_markup(self):
        # Importação local para evitar dependência circular
        if not self.linemarkup.text():  # Verificar se o campo está vazio
            QMessageBox.warning(self, "Erro", "O campo de markup está vazio.")
            return

        markup_value = float(self.linemarkup.text().replace(',', '.'))
        produto = ProdutoView()
        precocomp = produto.precounid.text()  # Obter o valor do campo linemarkup
        if precocomp == '':
            QMessageBox.warning(self, "Erro", "O campo de preço de custo está vazio.")
            return
        else:
            precocomp = float(precocomp.replace(',', '.'))
            markup_produdto = float(self.linemarkup.text().replace(',', '.'))
            mk = float(precocomp) + markup_produdto

            produto.linemarkup.setText(str(markup_produdto).replace('.',','))
            produto.precovenda.setText("{:.2f}".format(mk).replace('.',','))
            self.close()
            produto.show()

