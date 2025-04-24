from utils.database import Database

class Produto:
    def __init__(self, ean, descricao,grupo, fabricante,unidade,precocomp,precovenda):
        self.lineID = None
        self.ean = ean
        self.descricao = descricao 
        self.grupo = grupo
        self.fabricante = fabricante
        self.unidade = unidade
        self.precocomp = precocomp
        self.precovenda = precovenda
    
    def cadastro_produto(self):
        # Aqui você pode adicionar a lógica para cadastrar o produto no banco de dados ou em outro lugar
        try:
            query = "INSERT INTO tblproduto (ean, descricao, categoria, fabricante, unidade, precocusto, precovenda) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (self.ean, self.descricao, self.grupo, self.fabricante, self.unidade, self.precocomp, self.precovenda)
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
                 (self.ean, self.descricao, self.grupo, self.fabricante, self.unidade, self.precocomp, self.precovenda, self.ean))
    def excluir_produto(self):
        # Aqui você pode adicionar a lógica para excluir o produto do banco de dados ou em outro lugar
        db = Database()
        return db.delete_id("tblproduto", "ean", self.ean)

    def buscar_produto(self):
        try:
            db = Database()
            produto = db.select_id("tblproduto", "ean", self.ean)
            if produto:
                return {
                    "ean": produto[0],
                    "descricao": produto[1],
                    "grupo": produto[2],
                    "fabricante": produto[3],
                    "unidade": produto[4],
                    "precocomp": produto[5],
                    "precovenda": produto[6],
                }
            return None
        except Exception as e:
            print(f"Erro ao buscar produto: {e}")
            return None
