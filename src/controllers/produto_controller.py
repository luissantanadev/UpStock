from src.models.produto import Produto

class ProdutoController:
    def cadastrar_produto(self, produto: Produto):
        # Ajuste para usar o objeto Produto
        return {
            "codigo": produto.ean,
            "descricao": produto.descricao,
            "grupo": produto.grupo,
            "fabricante": produto.fabricante,
            "unidade": produto.unidade,
            "precocomp": produto.precocomp,
            "precovenda": produto.precovenda
        }
