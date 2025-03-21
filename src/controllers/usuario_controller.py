from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def cadastrar(nome, login, senha):
        novousuario = Usuario(nome, login, senha)
        return novousuario.cadastrar()
    @staticmethod
    def verificar_login(login, senha):
        # Verifica se o usuário e senha estão corretos
        return Usuario.verificar(login, senha)