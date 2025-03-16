# controllers/cliente_controller.py

from src.models.cliente import Cliente

class ClienteController:
    def __init__(self):
        pass  # Podemos adicionar alguma lógica futura, como logs ou cache

    def cadastrar_cliente(self, cnpjcpf, descricao, cep, endereco, bairro, cidade, uf, telefone=None, celular=None, email=None):
        """
        Cadastra um novo cliente no banco de dados.
        """
        try:
            cliente = Cliente(
                cnpjcpf=cnpjcpf, descricao=descricao, cep=cep, endereco=endereco, 
                bairro=bairro, cidade=cidade, uf=uf, telefone=telefone, celular=celular, email=email
            )
            cliente.save()
            return f"Cliente {cliente.descricao} cadastrado com sucesso!"
        except Exception as e:
            return f"Erro ao cadastrar cliente: {str(e)}"

    def atualizar_cliente(self, idcliente, cnpjcpf, descricao, cep, endereco, bairro, cidade, uf, telefone=None, celular=None, email=None):
        """
        Atualiza os dados de um cliente existente.
        """
        try:
            cliente = Cliente.get_by_id(idcliente)
            if not cliente:
                return "Cliente não encontrado."

            cliente.cnpjcpf = cnpjcpf
            cliente.descricao = descricao
            cliente.cep = cep
            cliente.endereco = endereco
            cliente.bairro = bairro
            cliente.cidade = cidade
            cliente.uf = uf
            cliente.telefone = telefone
            cliente.celular = celular
            cliente.email = email
            cliente.save()
            return f"Cliente {cliente.descricao} atualizado com sucesso!"
        except Exception as e:
            return f"Erro ao atualizar cliente: {str(e)}"

    def buscar_cliente_por_id(self, idcliente):
        """
        Retorna os dados de um cliente pelo ID.
        """
        try:
            cliente = Cliente.get_by_id(idcliente)
            if cliente:
                return {
                    "idcliente": cliente.idcliente,
                    "cnpjcpf": cliente.cnpjcpf,
                    "descricao": cliente.descricao,
                    "cep": cliente.cep,
                    "endereco": cliente.endereco,
                    "bairro": cliente.bairro,
                    "cidade": cliente.cidade,
                    "uf": cliente.uf,
                    "telefone": cliente.telefone,
                    "celular": cliente.celular,
                    "email": cliente.email
                }
            else:
                return "Cliente não encontrado."
        except Exception as e:
            return f"Erro ao buscar cliente: {str(e)}"

    def excluir_cliente(self, idcliente):
        """
        Remove um cliente do banco de dados pelo ID.
        """
        try:
            cliente = Cliente.get_by_id(idcliente)
            if not cliente:
                return "Cliente não encontrado."

            cliente.delete()
            return f"Cliente {cliente.idcliente} excluído com sucesso!"
        except Exception as e:
            return f"Erro ao excluir cliente: {str(e)}"
