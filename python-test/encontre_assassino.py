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

			return erros[randint(0 ,len(erros)-1)]

	def filter(self,obj, arr):
		retorno = []
		for a in arr:
			if(a !=obj):
				retorno.append(a)
		return retorno

	def resolver_crime(self):
		resposta = -1
		while(resposta != 0):
			suspeito = self.suspeitos[randint(0,len(self.suspeitos)-1)]
			possivel_arma = self.armas[randint(0,len(self.armas)-1)]
			possivel_local = self.locais[randint(0,len(self.locais)-1)]

			resposta = self.descobrir_assassino(suspeito, possivel_arma, possivel_local)

			if(resposta == 1):
				self.suspeitos = self.filter(suspeito, self.suspeitos)
			
			if(resposta == 2):
				self.armas = self.filter(possivel_arma, self.armas)

			if (resposta == 3):
				self.locais = self.filter(possivel_local, self.locais)

		return {"suspeito" : suspeito, "arma" : possivel_arma, "local" : possivel_local}

def main():
    unittest.main()

if __name__ == '__main__':
    main()
