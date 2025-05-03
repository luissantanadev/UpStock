from src.models.produto import Produto

class ProdutoController:
    def cadastrar_produto(self, produto: Produto):
        try:
            return produto.cadastro_produto()
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return False
    def atualizar_produto(self, produto: Produto):
        try:
            return produto.atualizar_produto()
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            return False
    def excluir_produto(self, produto: Produto):
        try:
            return produto.excluir_produto()
        except Exception as e:
            print(f"Erro ao excluir produto: {e}")
            return False
    def listar_produtos(self):
        try:
            return Produto.listar_produtos()
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return []
    def listar_produto_id(self, id_produto):
        try:
            return Produto.listar_produto_id(id_produto)
        except Exception as e:
            print(f"Erro ao listar produto por ID: {e}")
            return None
    def pesquisar_produto(self, ean):
        try:
            return Produto.listar_produto_id(ean)
        except Exception as e:
            print(f"Erro ao pesquisar produto: {e}")
            return None
