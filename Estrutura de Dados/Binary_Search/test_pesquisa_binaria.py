import unittest
from pesquisa_binaria import PesquisaBinaria

class TestPesquisaBinaria(unittest.TestCase):

    def setUp(self):
        self.pb = PesquisaBinaria()
        self.lista_exemplo = [1, 3, 5, 7, 9]

    def test_busca_iterativa_encontra_elemento(self):
        self.assertEqual(self.pb.busca_iterativa(self.lista_exemplo, 3), 1)
        self.assertEqual(self.pb.busca_iterativa(self.lista_exemplo, 9), 4)

    def test_busca_iterativa_nao_encontra_elemento(self):
        self.assertIsNone(self.pb.busca_iterativa(self.lista_exemplo, -1))
        self.assertIsNone(self.pb.busca_iterativa(self.lista_exemplo, 10))

    def test_busca_recursiva_encontra_elemento(self):
        self.assertEqual(self.pb.busca_recursiva(self.lista_exemplo, 0, len(self.lista_exemplo) - 1, 3), 1)
        self.assertEqual(self.pb.busca_recursiva(self.lista_exemplo, 0, len(self.lista_exemplo) - 1, 9), 4)

    def test_busca_recursiva_nao_encontra_elemento(self):
        self.assertIsNone(self.pb.busca_recursiva(self.lista_exemplo, 0, len(self.lista_exemplo) - 1, -1))
        self.assertIsNone(self.pb.busca_recursiva(self.lista_exemplo, 0, len(self.lista_exemplo) - 1, 10))

if __name__ == '__main__':
    unittest.main()
    