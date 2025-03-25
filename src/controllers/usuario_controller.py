from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def cadastrar(nome, login, senha):
        novousuario = Usuario(nome, login, senha)
        return novousuario.salvar()
    @staticmethod
    def verificar_login(login, senha):
        print(f"Verificando login para {login} com senha {senha}")
        # Verifica se o login e senha estão corretos
        return Usuario.verificar(login, senha)

    @staticmethod
    def atualizar_senha(login, nova_senha):
        print(f"Atualizando senha para {login}")
        # Atualiza a senha do usuário
        return Usuario.atualizar_senha(login, nova_senha)
