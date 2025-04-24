from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIntValidator, QDoubleValidator
import os
from PyQt5.QtWidgets import QLineEdit, QPushButton
from controllers.produto_controller import ProdutoController
from PyQt5.QtWidgets import QMessageBox

class ProdutoView(QMainWindow):
    def __init__(self, parent=None):
        super(ProdutoView, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'screens', 'frm_produto.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Cadastro de Produtos")
        #self.setGeometry(100, 100, 800, 600)
        
        # elementos da interface
        self.line_ean = self.findChild(QLineEdit, 'line_ean')
        self.line_descricao = self.findChild(QLineEdit, 'line_descricao')
        self.line_grupo = self.findChild(QLineEdit, 'line_grupo')
        self.line_fabric = self.findChild(QLineEdit, 'line_fabric')
        self.line_tipo_und = self.findChild(QLineEdit, 'line_tipo_und')
        self.precounid = self.findChild(QLineEdit, 'precounid')  
        self.precovenda = self.findChild(QLineEdit, 'precovenda')
        self.lineID = self.findChild(QLineEdit, 'lineID')
        # Configurar validação dos campos
        int_validator = QIntValidator()  # Validador de números inteiros
        double_validator = QDoubleValidator()  # Validador de números decimais
        self.line_ean.setValidator(int_validator)
        self.precounid.setValidator(double_validator)
        self.precovenda.setValidator(double_validator)

        # botões
        self.btnPesquisa = self.findChild(QPushButton, 'btnPesquisa')
        self.pushButton = self.findChild(QPushButton, 'pushButton')
        self.btnSalvar = self.findChild(QPushButton, 'btnSalvar')
        # Conectando os botões aos métodos
        self.btnPesquisa.clicked.connect(self.pesquisar_produto)
        self.pushButton.clicked.connect(self.limpar_campos)
        self.btnSalvar.clicked.connect(self.salvar_produto)
        # Conectar os campos ao método de capitalização
        self.line_descricao.textChanged.connect(self.forcar_maiusculas)
        self.line_grupo.textChanged.connect(self.forcar_maiusculas)
        self.line_fabric.textChanged.connect(self.forcar_maiusculas)
        self.line_tipo_und.textChanged.connect(self.forcar_maiusculas)

    def forcar_maiusculas(self):
        # Atualiza o texto dos campos para maiúsculas
        self.line_descricao.setText(self.line_descricao.text().upper())
        self.line_grupo.setText(self.line_grupo.text().upper())
        self.line_fabric.setText(self.line_fabric.text().upper())
        self.line_tipo_und.setText(self.line_tipo_und.text().upper())

    def pesquisar_produto(self):
        ean = self.line_ean.text()
        if not ean:
            QMessageBox.warning(self, "Erro", "Preencha o campo EAN.")
            return
        produto = ProdutoController.pesquisar_produto(ean)
        if produto:
            self.preencher_campos(produto)
        else:
            QMessageBox.information(self, "Resultado", "Produto não encontrado.")
    def salvar_produto(self):
        try:
            ean = self.line_ean.text()
            descricao = self.line_descricao.text()
            grupo = self.line_grupo.text()
            fabricante = self.line_fabric.text()
            tipo_und = self.line_tipo_und.text()
            precounid = self.precounid.text().replace(',', '.').strip()
            precovenda = self.precovenda.text().replace(',', '.').strip()

            # Validação de campos numéricos
            try:
                precounid = float(precounid)
                precovenda = float(precovenda)
            except ValueError:
                QMessageBox.warning(self, "Erro", "Preencha os campos de preço corretamente.")
                return

            if not all([ean, descricao, grupo, fabricante, tipo_und]):
                QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
                return

            if ProdutoController.cadastrar_produto(ean, descricao, grupo, fabricante, tipo_und, precounid, precovenda):
                QMessageBox.information(self, "Sucesso", "Produto salvo com sucesso.")
                self.limpar_campos()
            else:
                QMessageBox.warning(self, "Erro", "Erro ao salvar o produto.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")

    def limpar_campos(self):
        self.line_ean.clear()
        self.line_descricao.clear()
        self.line_grupo.clear()
        self.line_fabric.clear()
        self.line_tipo_und.clear()
        self.precounid.clear()
        self.precovenda.clear()
        self.lineID.clear()
    def preencher_campos(self, produto):
        try:
            self.line_ean.setText(produto.get('ean', ''))
            self.line_descricao.setText(produto.get('descricao', ''))
            self.line_grupo.setText(produto.get('grupo', ''))
            self.line_fabric.setText(produto.get('fabricante', ''))
            self.line_tipo_und.setText(produto.get('unidade', ''))
            self.precounid.setText(str(produto.get('precocomp', '')))
            self.precovenda.setText(str(produto.get('precovenda', '')))
            self.lineID.setText(str(produto.get('id_produto', '')))
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao preencher campos: {e}")

