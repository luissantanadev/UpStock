import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils')))
from src.utils.database import Database
from src.models.usuario import Usuario
from src.controllers.usuario_controller import UsuarioController
from src.views.principal_view import PrincipalView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton
import mysql.connector
import mysql.connector.errors

app = QApplication(sys.argv)  # Adicionando a criação do QApplication

data = Database()
try:
    data = Database()
    print("Conexão com o banco de dados estabelecida.")
    # Exemplo de operação de inserção
    login = "adm"
    senha = "adm"
    
    print("****************************************************************************")
    test_controller = UsuarioController.verificar_login(login, senha)
    print(f"print 'test_controller', {test_controller}")
    if test_controller == True:
        tela = PrincipalView()
        tela.show()
        print("Usuário autenticado com sucesso.")
    else:
        print("Falha na autenticação do usuário.")

    # Exemplo de operação de seleção
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if data.connection:
        data.close()

sys.exit(app.exec_())  # Adicionando a execução do loop de eventos do QApplication