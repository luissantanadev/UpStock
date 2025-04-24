import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils')))
from src.models.produto import Produto
from unittest.mock import patch, MagicMock

class TestProduto(unittest.TestCase):
    def setUp(self):
        self.produto = Produto(
            ean="1234567890123",
            descricao="Produto Teste",
            grupo="Categoria Teste",
            fabricante="Fabricante Teste",
            unidade="Unidade Teste",
            precocomp=10.0,
            precovenda=15.0
        )

    @patch("src.models.produto.Database")
    def test_cadastro_produto_sucesso(self, MockDatabase):
        mock_db = MockDatabase.return_value
        mock_db.execute.return_value = True

        resultado = self.produto.cadastro_produto()
        self.assertTrue(resultado)
        mock_db.execute.assert_called_once()

    @patch("src.models.produto.Database")
    def test_cadastro_produto_falha(self, MockDatabase):
        mock_db = MockDatabase.return_value
        mock_db.execute.side_effect = Exception("Erro no banco de dados")

        resultado = self.produto.cadastro_produto()
        self.assertFalse(resultado)
        mock_db.execute.assert_called_once()

if __name__ == "__main__":
    unittest.main()
