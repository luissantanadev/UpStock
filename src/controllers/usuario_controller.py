from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def cadastrar(nome, login, senha):
        novousuario = Usuario(nome, login, senha)
        return novousuario.cadastrar()
    @staticmethod
    def verificar_login(login, senha):
        user = Usuario.verificar(login, senha)  # Certifique-se de que a classe Usuario aceita esses argumentos
        if user[0][1] == login and user[0][2] == senha:
            print("Login e senha corretos.")
            return True
        else:
            print("Login ou senha incorretos.")
            return False
    @staticmethod
    def atualizar_senha(login, nova_senha):
        print(f"Atualizando senha para {login}")
        # Atualiza a senha do usuário
        return Usuario.atualizar_senha(login, nova_senha)
    @staticmethod
    def novo_metodo_verificar_login(login, senha):
        # Verifica se o usuário e senha estão corretos usando um novo método
        return Usuario.novo_metodo_verificar(login, senha)
