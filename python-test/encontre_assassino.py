from random import randint

class Detetive:

	def __init__ (self, assassino, arma, local):
		self.assassino = assassino
		self.arma = arma
		self.local = local	
		self.suspeitos = [0, 1, 2, 3, 4, 5]
		self.locais = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.armas = [0, 1, 2, 3, 4, 5]

	def descobrir_assassino(self, suspeito, arma_chutado, local_chutado):
		if(self.assassino == suspeito and self.arma == arma_chutado and self.local == local_chutado):
			return 0
		else:
			erros = []
			if(self.assassino != suspeito):
				erros.append(1)
			if(self.arma != arma_chutado):
				erros.append(2)
			if(self.local != local_chutado):
				erros.append(3)

			# if(erros.length == 1)
			# 	return erros[0]
			# else
			return erros[randint(0 ,len(erros)-1)]

	def ehSuspeito(self, suspeito):
		return suspeito in self.suspeitos

	def ehLocalPossivel(self, local_possivel):
		return local_possivel in self.locais

	def ehArmaPossivel(self, arma_possivel):
		return arma_possivel in self.armas



