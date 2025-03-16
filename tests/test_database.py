import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from src.utils.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db.close()

    def test_select_all(self):
        result = self.db.select_all("usuarios")
        self.assertIsNotNone(result)

    def test_select_id(self):
        result = self.db.select_id("usuarios", "id", 1)
        self.assertIsNotNone(result)

    def test_insert_all(self):
        values = {"nome": "Teste", "email": "teste@example.com"}
        self.db.insert_all("usuarios", values)
        result = self.db.select_id("usuarios", "email", "teste@example.com")
        self.assertIsNotNone(result)

    def test_update(self):
        values = {"nome": "Teste Atualizado"}
        self.db.update("usuarios", values, "id", 1)
        result = self.db.select_id("usuarios", "id", 1)
        self.assertEqual(result["nome"], "Teste Atualizado")

    def test_delete_id(self):
        self.db.delete_id("usuarios", "id", 1)
        result = self.db.select_id("usuarios", "id", 1)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()