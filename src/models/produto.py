from utils.database import Database

class Produto:
    def __init__(self, ean, descricao,Grupo, fabricante,unidade,precocomp,precovenda):
        self.lineID = None
        self.ean = ean
        self.Descricao = descricao 
        self.Grupo = Grupo
        self.fabricante = fabricante
        self.unidade = unidade
        self.precocomp = precocomp
        self.precovenda = precovenda

    
    def calcular_markup(self):
        if self.precocomp == 0:
            raise ValueError("O preço de custo não pode ser zero para calcular o markup.")
    def cadastro_produto(self):
        # Aqui você pode adicionar a lógica para cadastrar o produto no banco de dados ou em outro lugar
        try:
            query = "INSERT INTO tblproduto (ean, descricao, categoria, fabricante, unidade, precocusto, markup, precovenda) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (self.ean, self.Descricao, self.Grupo, self.fabricante, self.unidade, self.precocomp, self.precovenda)
            # Execute a consulta no banco de dados aqui
            db = Database()
            return db.execute(query, values)
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return False

    def atualizar_produto(self):
        # Aqui você pode adicionar a lógica para atualizar o produto no banco de dados ou em outro lugar
        db = Database()
        return db.execute("UPDATE tblproduto SET ean = %s, descricao = %s, categoria = %s, fabricante = %s, unidade = %s, precocusto = %s,precovenda = %s WHERE ean = %s",
                 (self.ean, self.Descricao, self.Grupo, self.fabricante, self.unidade, self.precocomp, self.precovenda, self.ean))
    def excluir_produto(self):
        # Aqui você pode adicionar a lógica para excluir o produto do banco de dados ou em outro lugar
        db = Database()
        return db.delete_id("tblproduto", "ean", self.ean)

    def buscar_produto(self):
        # Aqui você pode adicionar a lógica para buscar o produto no banco de dados ou em outro lugar
        db = Database()
        return db.select_id("tblproduto", "ean", self.ean) 
