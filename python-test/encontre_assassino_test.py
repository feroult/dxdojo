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
		detetive = Detetive(0,0,0)
		for i in detetive.suspeitos:
			self.assertTrue(detetive.ehSuspeito(i))

		for i in detetive.locais:
			self.assertTrue(detetive.ehLocalPossivel(i))

		for i in detetive.armas:
			self.assertTrue(detetive.ehArmaPossivel(i))
			
		#self.assertTrue(detetive.arma(i))
		#self.assertTrue(detetive.local(i))	

	# def test_memoria_do_detetive(self):
	# 	detetive = Detetive(0,0,0)

	# 	detetive.descobrir_assassino(1, 0, 0)
	# 	assertFalse(detetive.suspeito(1));



def main():
    unittest.main()

if __name__ == '__main__':
    main()