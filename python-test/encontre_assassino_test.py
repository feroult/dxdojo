import unittest
from encontre_assassino import Detetive
 
class Encontre_Assassino_Test(unittest.TestCase):
	
	def test_teoria_certa(self):
		detetive = Detetive(0, 0, 0)
		self.assertEqual(0, detetive.descobrir_assassino(0, 0, 0))

	def test_apenas_um_erro(self):
		detetive = Detetive(0, 0, 0)
		self.assertEqual(1, detetive.descobrir_assassino(1, 0, 0))
		self.assertEqual(2, detetive.descobrir_assassino(0, 1, 0))
		self.assertEqual(3, detetive.descobrir_assassino(0, 0, 1))

	def test_dois_erros(self):
		detetive = Detetive(0,0,0)
		contemErro = detetive.descobrir_assassino(0,1,1) in [2,3]
		self.assertTrue(contemErro)

	def test_inicio_do_jogo(self):
		detetive = Detetive(1,3,5)
		dados_do_crime = detetive.resolver_crime()
		self.assertEqual(1, dados_do_crime["suspeito"])
		self.assertEqual(3, dados_do_crime["arma"])
		self.assertEqual(5, dados_do_crime["local"])


def main():
    unittest.main()

if __name__ == '__main__':
    main()