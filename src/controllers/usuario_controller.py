from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def cadastrar(nome, login, senha):
        novousuario = Usuario(nome, login, senha)
        return novousuario.salvar()
    @staticmethod
    def verificar_login(login, senha):
        user = Usuario.verificar(login, senha)  
        if not user:
            return False  # Login inválido
        user_login = user["login"]
        user_senha = user["senha"]
        return user_login == login and user_senha == senha

    @staticmethod
    def atualizar_senha(login, nova_senha):
        print(f"Atualizando senha para {login}")
        # Atualiza a senha do usuário
        return Usuario.atualizar_senha(login, nova_senha)
