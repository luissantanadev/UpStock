from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def cadastrar(nome, email, senha):
        novousuario = Usuario(nome, email, senha)
        return novousuario.cadastrar()