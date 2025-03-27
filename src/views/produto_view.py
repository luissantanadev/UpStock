from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
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
        self.linemarkup = self.findChild(QLineEdit, 'linemarkup')
        self.lineID = self.findChild(QLineEdit, 'lineID')
        # botões
        self.btnPesquisa = self.findChild(QPushButton, 'btnPesquisa')
        self.pushButton = self.findChild(QPushButton, 'pushButton')
        self.btnSalvar = self.findChild(QPushButton, 'btnSalvar')
        self.btn_calc_markup = self.findChild(QPushButton, 'btn_calc_markup')
    # Conectando os botões aos métodos
        self.btnPesquisa.clicked.connect(self.pesquisar_produto)
        self.pushButton.clicked.connect(self.limpar_campos)
        self.btnSalvar.clicked.connect(self.salvar_produto)
        self.btn_calc_markup.clicked.connect(self.calcular_markup)
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
        ean = self.line_ean.text()
        descricao = self.line_descricao.text()
        grupo = self.line_grupo.text()
        fabricante = self.line_fabric.text()
        tipo_und = self.line_tipo_und.text()
        precounid = self.precounid.text()
        precovenda = self.precovenda.text()
        markup = self.linemarkup.text()
        id_produto = self.lineID.text()

        if not all([ean, descricao, grupo, fabricante, tipo_und, precounid, precovenda]):
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        if ProdutoController.cadastrar_produto(ean, descricao, grupo, fabricante, tipo_und, precounid, precovenda, markup):
            QMessageBox.information(self, "Sucesso", "Produto salvo com sucesso.")
            self.limpar_campos()
        else:
            QMessageBox.warning(self, "Erro", "Erro ao salvar o produto.")
    def limpar_campos(self):
        self.line_ean.clear()
        self.line_descricao.clear()
        self.line_grupo.clear()
        self.line_fabric.clear()
        self.line_tipo_und.clear()
        self.precounid.clear()
        self.precovenda.clear()
        self.linemarkup.clear()
        self.lineID.clear()
    def preencher_campos(self, produto):
        self.line_ean.setText(produto['ean'])
        self.line_descricao.setText(produto['descricao'])
        self.line_grupo.setText(produto['grupo'])
        self.line_fabric.setText(produto['fabricante'])
        self.line_tipo_und.setText(produto['tipo_und'])
        self.precounid.setText(str(produto['precounid']))
        self.precovenda.setText(str(produto['precovenda']))
        self.linemarkup.setText(str(produto['markup']))
        self.lineID.setText(str(produto['id_produto']))
    def calcular_markup(self):
        pass
    