from PyQt5.QtWidgets import QApplication
from views.principal_view import PrincipalView
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrincipalView()  # Cria a janela principal
    window.show()  # Exibe a janela
    sys.exit(app.exec_())  # Mantém o loop da aplicação rodando
