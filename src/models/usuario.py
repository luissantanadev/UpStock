from utils.database import Database

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    def salvar(self):
        # Salva o usuário no banco de dados
        db = Database()
        db.conectar()
        query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        values = (self.nome, self.email, self.senha)
        return db.execute(query, values)