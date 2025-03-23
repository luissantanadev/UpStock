from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def cadastrar(nome, login, senha):
        novousuario = Usuario(nome, login, senha)
        return novousuario.salvar()
    @staticmethod
    def verificar_login(login, senha):
        user = Usuario.verificar(login, senha) 
        print(f"Verificando login: {login}, senha: {senha}")
        print(f"Resultado da verificação: {user}")
        if not user:
            return False  # Login inválido
        return user["login"] == login and user["senha"] == senha

    @staticmethod
    def atualizar_senha(login, nova_senha):
        print(f"Atualizando senha para {login}")
        # Atualiza a senha do usuário
        return Usuario.atualizar_senha(login, nova_senha)
