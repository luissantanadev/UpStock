import sys
import os

# Verifica se o módulo 'os' está sendo sobrescrito por um arquivo local
if os.path.basename(__file__) == 'os.py':
    raise ImportError("Renomeie o arquivo 'os.py' para evitar conflitos com o módulo padrão do Python")

from PyQt5.QtWidgets import QApplication
from views.login_view import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginView()  # Cria a janela principal
    window.show()  # Exibe a janela
    sys.exit(app.exec_())  # Mantém o loop da aplicação rodando
