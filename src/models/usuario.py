from utils.database import Database
import mysql.connector
import mysql.connector.errors

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
        try:
            db = Database()
            # Verifica se o login e senha estão corretos
            query = "SELECT * FROM tbllogin WHERE login = %s AND senha = %s"
            resultado = db.fetch_one(query, (login, senha))
            print(f"Resultado da verificação do bando de dados: {resultado}")  # Depuração
            return resultado  # Retorna True se o login for válido
        except mysql.connector.Error as err:
            print(f"Erro ao verificar login: {err}")
            return err

    def atualizar_senha(self,login, nova_senha):
        db = Database()
        # Atualiza a senha do usuário no banco de dados
        query = "UPDATE tbllogin SET senha = %s WHERE login = %s"
        values = (nova_senha, login)
        return db.execute(query, values)