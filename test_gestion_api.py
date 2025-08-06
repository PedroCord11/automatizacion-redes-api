import unittest
from gestion_api import listar_dispositivos, BASE_URL

class TestGestionAPI(unittest.TestCase):

    def test_listar_dispositivos_exitoso(self):
        dispositivos = listar_dispositivos()
        
        self.assertIsNotNone(dispositivos)
        self.assertIn('data', dispositivos)
        self.assertGreater(len(dispositivos['data']), 0)
        self.assertIsInstance(dispositivos['data'], list)

    def test_listar_dispositivos_error_url_invalida(self):
        global BASE_URL
        original_url = BASE_URL
        BASE_URL = "https://reqres.in/api/users_fail"
        
        dispositivos = listar_dispositivos()
        
        self.assertIsNone(dispositivos)
        
        BASE_URL = original_url

if __name__ == '__main__':
    unittest.main()
