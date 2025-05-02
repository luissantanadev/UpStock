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

        # Conectando botões às funções
        self.actionProdutos.triggered.connect(self.abrir_produto)
        self.actionCaixa.triggered.connect(self.abrir_caixa)
        self.actionUser.triggered.connect(self.abrir_usuario)
        self.actionClientes.triggered.connect(self.abrir_cliente_cadastro)
        self.actionEstoque.triggered.connect(self.abrir_estoque)
        #self.actionRelatorio.triggered.connect(self.abrir_relatorio)

    def abrir_produto(self):
        from views.produto_view import ProdutoView
        self.produto_view = ProdutoView()
        self.produto_view.show()
    
    def abrir_caixa(self):
        from views.venda_view import CaixaView
        self.caixa_view = CaixaView()
        self.caixa_view.show()

    def abrir_usuario(self):
        from src.views.usuario_view import UsuarioView
        self.usuario_view = UsuarioView()
        self.usuario_view.show()
    
    def abrir_cliente_pesquisa(self):
        from views.cliente_pesquisar_view import ClientePesquisaView
        self.cliente_view = ClientePesquisaView()
        self.cliente_view.show()
    def abrir_cliente_cadastro(self):
        from views.cliente_cad_view import ClienteCadView
        self.cliente_view = ClienteCadView()
        self.cliente_view.show()
    def abrir_estoque(self):
        from src.views.estoque_view import EstoqueView
        self.estoque_view = EstoqueView()
        self.estoque_view.show()
    
    """def abrir_relatorio(self):
        from src.views.relatorio_view import RelatorioView
        self.relatorio_view = RelatorioView()
        self.relatorio_view.show()"""
