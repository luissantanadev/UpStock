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

    def execute(self, query, params=None):
        """Executa um comando SQL e retorna o cursor"""
        self.cursor.execute(query, params or ())
        self.connection.commit()
        return self.cursor

    def fetch_one(self, query, params=None):
        """Executa um comando SQL e retorna um único resultado"""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def commit(self):
        """Confirma as alterações no banco de dados"""
        self.connection.commit()

    def close(self):
        """Fechar a conexão com o banco de dados""" 
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def select_all(self, table):
        """Selecionar todos os registros da tabela especificada"""
        try:
            sql = f"SELECT * FROM {table}"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except mysql.connector.Error as err:
            return None

    def select_id(self, table, id_column, id):
        """Selecionar um registro da tabela especificada pelo ID"""
        try:
            sql = f"SELECT * FROM {table} WHERE {id_column} = %s"
            self.cursor.execute(sql, (id,))
            row = self.cursor.fetchone()
            return row
        except mysql.connector.Error as err:
            return None

    def insert_all(self, table, values):
        """Inserir um dicionário de valores na tabela especificada"""
        try:
            columns = ", ".join(values.keys())
            placeholders = ", ".join("%s" for _ in values.values())
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(values.values()))
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()

    def update(self, table, values, id_column, id):
        """Atualizar um registro na tabela especificada"""
        try:
            set_clause = ", ".join(f"{key} = %s" for key in values.keys())
            sql = f"UPDATE {table} SET {set_clause} WHERE {id_column} = %s"
            self.cursor.execute(sql, (*values.values(), id))
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()

    def delete_all(self, table):
        """Excluir um registro da tabela especificada"""
        try:
            sql = f"DELETE * FROM {table}"
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()

    def delete_id(self, table, id_column, id): 
        """Excluir um registro da tabela especificada pelo ID"""
        try:
            sql = f"DELETE FROM {table} WHERE {id_column} = %s"
            self.cursor.execute(sql, (id,))
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
