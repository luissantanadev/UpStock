# UpStock

UpStock é um projeto para gerenciar um banco de dados MySQL usando Python. Ele inclui funcionalidades para conectar, inserir, selecionar, atualizar e excluir registros no banco de dados.

## Requisitos

- Python 3.x
- PyQt5
- mysql-connector-python

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/upstock.git
    cd upstock
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Banco de Dados

1. Crie um banco de dados MySQL chamado `dbstore`.
2. Atualize as credenciais de conexão no arquivo `database.py` conforme necessário.

## Uso

### Executar o projeto

Execute o script `main.py` para iniciar o projeto:
```bash
python main.py
```

## Estrutura do Projeto

- `database.py`: Contém a classe `Database` com métodos para manipulação do banco de dados.
- `main.py`: Script principal para executar o projeto.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-nova-funcionalidade`.
3. Faça suas alterações e commit: `git commit -m 'Adiciona nova funcionalidade'`.
4. Envie para o branch original: `git push origin minha-nova-funcionalidade`.
5. Crie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
