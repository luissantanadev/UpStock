# models/cliente.py

from src.utils.database import Database

class Cliente:
    def __init__(self, idcliente=None, cnpjcpf=None, descricao=None, cep=None, endereco=None, bairro=None, cidade=None, uf=None, telefone=None, celular=None, email=None):
        self.idcliente = idcliente
        self.cnpjcpf = cnpjcpf
        self.descricao = descricao
        self.cep = cep
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.db = Database()

    def save(self):
        """
        Salva o cliente no banco de dados.
        Se idcliente for None, insere um novo registro; caso contrário, atualiza o registro existente.
        """
        if self.idcliente is None:
            query = """
                INSERT INTO tblcliente (cnpjcpf, descricao, cep, endereco, bairro, cidade, uf, telefone, celular, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (self.cnpjcpf, self.descricao, self.cep, self.endereco, self.bairro, self.cidade, self.uf, self.telefone, self.celular, self.email)
            cursor = self.db.execute(query, params)
            self.idcliente = cursor.lastrowid  # Pega o ID gerado pelo banco
            self.db.connection.commit()
        else:
            query = """
                UPDATE tblcliente 
                SET cnpjcpf=%s, descricao=%s, cep=%s, endereco=%s, bairro=%s, cidade=%s, uf=%s, telefone=%s, celular=%s, email=%s
                WHERE idcliente=%s
            """
            params = (self.cnpjcpf, self.descricao, self.cep, self.endereco, self.bairro, self.cidade, 
                      self.uf, self.telefone, self.celular, self.email, self.idcliente)
            self.db.execute(query, params)
            self.db.connection.commit()

    @staticmethod
    def get_by_id(idcliente):
        """Busca um cliente pelo ID"""
        db = Database()
        query = "SELECT * FROM tblcliente WHERE idcliente = %s"
        
        cursor = db.execute(query, (idcliente,))
        cliente_data = cursor.fetchone()
        db.close()
        
        if cliente_data:
            return Cliente(**cliente_data)
        return None

    def delete(self):
        """
        Remove o cliente do banco de dados.
        """
        if self.idcliente:
            query = "DELETE FROM tblcliente WHERE idcliente = %s"
            self.db.execute(query, (self.idcliente,))
            self.db.connection.commit()
            self.idcliente = None
