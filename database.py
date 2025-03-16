import mysql.connector
import mysql.connector.errors

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect(mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1@!Cofggcvf",
            database="dbstore"
        ))  # Conectar ao banco de dados

    def connect(self, connection):  
        """Conectar ao banco de dados"""
        self.connection = connection
        self.cursor = self.connection.cursor(dictionary=True)
        print("Conectado ao banco de dados")

    def close(self):
        """Fechar a conexão com o banco de dados""" 
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados fechada")

    def select_all(self, table):
        """Selecionar todos os registros da tabela especificada"""
        try:
            sql = f"SELECT * FROM {table}"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None

    def select_id(self, table, id_column, id):
        """Selecionar um registro da tabela especificada pelo ID"""
        try:
            sql = f"SELECT * FROM {table} WHERE {id_column} = %s"
            self.cursor.execute(sql, (id,))
            row = self.cursor.fetchone()
            return row
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None

    def insert_all(self, table, values):
        """Inserir um dicionário de valores na tabela especificada"""
        try:
            columns = ", ".join(values.keys())
            placeholders = ", ".join("%s" for _ in values.values())
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(values.values()))
            self.connection.commit()
            print(f"Inserido {self.cursor.rowcount} linhas em {table}")
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            self.connection.rollback()

    def update(self, table, values, id_column, id):
        """Atualizar um registro na tabela especificada"""
        try:
            set_clause = ", ".join(f"{key} = %s" for key in values.keys())
            sql = f"UPDATE {table} SET {set_clause} WHERE {id_column} = %s"
            self.cursor.execute(sql, (*values.values(), id))
            self.connection.commit()
            print(f"Atualizado {self.cursor.rowcount} linhas em {table}")
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            self.connection.rollback()

    def delete_all(self, table):
        """Excluir um registro da tabela especificada"""
        try:
            sql = f"DELETE * FROM {table}"
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Excluído {self.cursor.rowcount} linhas de {table}")
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            self.connection.rollback()

    def delete_id(self, table, id_column, id): 
        """Excluir um registro da tabela especificada pelo ID"""
        try:
            sql = f"DELETE FROM {table} WHERE {id_column} = %s"
            self.cursor.execute(sql, (id,))
            self.connection.commit()
            print(f"Excluído {self.cursor.rowcount} linhas de {table}")
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            self.connection.rollback()

if __name__ == "__main__":
    # Exemplo de uso
    try:
        data = Database()
        print("Conexão com o banco de dados estabelecida.")
        # Exemplo de operação de inserção
        print(data.select_by_id("tbllogin","idlogin", 2))
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if data.connection:
            data.close()