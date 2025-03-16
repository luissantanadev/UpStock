import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils')))
from src.utils.database import Database
import mysql.connector
import mysql.connector.errors

data = Database()
try:
    data = Database()
    print("Conexão com o banco de dados estabelecida.")
    # Exemplo de operação de inserção
    print(data.select_id("tbllogin","idlogin", 2))
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if data.connection:
        data.close()