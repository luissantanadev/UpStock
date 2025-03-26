class Produto:
    def __init__(self, ean, descricao,Grupo, fabricante,unidade,precocomp,precovenda, markup):
        self.ean = ean
        self.Descricao = descricao 
        self.Grupo = Grupo
        self.fabricante = fabricante
        self.unidade = unidade
        self.precocomp = precocomp
        self.precovenda = precovenda
        self.markup = markup
    
    def calcular_markup(self):
        if self.precocomp == 0:
            raise ValueError("O preço de custo não pode ser zero para calcular o markup.")
    def cadastro_produto(self):
        # Aqui você pode adicionar a lógica para cadastrar o produto no banco de dados ou em outro lugar
        pass
    def atualizar_produto(self):
        # Aqui você pode adicionar a lógica para atualizar o produto no banco de dados ou em outro lugar
        pass
    def excluir_produto(self):
        # Aqui você pode adicionar a lógica para excluir o produto do banco de dados ou em outro lugar
        pass
    def buscar_produto(self):
        # Aqui você pode adicionar a lógica para buscar o produto no banco de dados ou em outro lugar
        pass

