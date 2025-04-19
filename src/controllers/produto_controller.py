from models.produto import Produto

class ProdutoController:
    @staticmethod
    def cadastrar_produto(ean, descricao, grupo, fabricante, unidade, precocomp, precovenda, markup):
        try:
            produto = Produto(ean, descricao, grupo, fabricante, unidade, precocomp, precovenda, markup)
            produto.cadastro_produto()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return False
    def pesquisar_produto(ean):
        try:
            produto = Produto(ean, "", "", "", "", 0, 0, 0)
            return produto.buscar_produto()
        except Exception as e:
            print(f"Erro ao pesquisar produto: {e}")
            return None
