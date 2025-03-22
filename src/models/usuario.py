from utils.database import Database

class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
    def salvar(self):
        # Salva o usuário no banco de dados
        db = Database()
        db.conectar()
        query = "INSERT INTO tbllogin (nome, login, senha) VALUES (%s, %s, %s)"
        values = (self.nome, self.login, self.senha)
        return db.execute(query, values)
    @staticmethod
    def verificar(login, senha):
        db = Database()
        # Verifica se o login e senha estão corretos
        query = "SELECT * FROM tbllogin WHERE login = '%s' AND senha = '%s'"
        values = (login, senha)
        resultado = db.fetch_one(query, values)
        return resultado  # Retorna True se o login for válido
    def atualizar_senha(self,login, nova_senha):
        db = Database()
        # Atualiza a senha do usuário no banco de dados
        query = "UPDATE tbllogin SET senha = %s WHERE login = %s"
        values = (nova_senha, login)
        return db.execute(query, values)