from models.produto import Produto

def cadastrar_produto(ean, descricao, grupo, fabricante, unidade, precocomp, precovenda, markup):
    try:
        produto = Produto(ean, descricao, grupo, fabricante, unidade, precocomp, precovenda, markup)
        produto.cadastro_produto()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
        return False