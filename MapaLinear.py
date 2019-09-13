# 2 <= qtde. de Municipios <= 10000
# 1 <= Partida/Chegada <= qtde. de Municipios
# 1 <= Distancia <= 100

from random import randint
Linearlandia = {}
Municipios = int(input("digite a quantidade de Municipios: "))
Partida = int(input("digite o 'ponto de partida: "))
Chegada = int(input("digite o ponto de chegada: "))

cont = 0
while cont != Municipios:
	CidadeAtual = Partida
	Estrada = randint(1,100)
	ProxCidade = randint(1,Municipios)
	Linearlandia[CidadeAtual] = [ProxCidade,Estrada]
	# if Linearlandia.has_key(CidadeAtual) == True:
	#  	 continue
	if cont == Municipios-1:
		ProxCidade = Chegada

def Distancia(Linearlandia, Partida, Chegada, Caminho=[]):
        Caminho += Partida
        if Partida == Chegada:
            return Caminho
        if not Linearlandia.has_key(Partida): # se não tiver a chave determinada
            return None
        for nodo in range(Partida,Linearlandia):
            if nodo not in Caminho:
                NovoCaminho = Distancia(Linearlandia, nodo, Chegada, Caminho)
                if NovoCaminho: return NovoCaminho
        return None
