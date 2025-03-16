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

## Uso

### Criar a tabela `login`

Execute o script `create_table.py` para criar a tabela `login` no banco de dados `dbstore`:
```bash
python create_table.py
```

### Executar o projeto

Execute o script `main.py` para iniciar o projeto:
```bash
python main.py
```

## Estrutura do Projeto

- `database.py`: Contém a classe `Database` com métodos para manipulação do banco de dados.
- `main.py`: Script principal para executar o projeto.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
