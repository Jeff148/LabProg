# IMCOMPLETO

# TotalCidades = de 2 a 100
# TotalVoos = de (TotalCidades-1) a 10**5
# Cidade1/Cidade2 = de 0 a (TotalCidades-1)
# DistanciaVoo = de 1 a 100

def dijkstra(grafo, origem):
# retorna a menor distancia de um dado nó para todos os outros possíveis.

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0
    
    for vertice in grafo.keys():
        naoVisitados.append(vertice) #inclui os vertices nos não visitados    
        distanciaAtual[vertice] = float('inf') #inicia os vertices como infinito

    distanciaAtual[atual] =0

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho] > pesoCalc:
                 distanciaAtual[vizinho] = pesoCalc
                 controle[vizinho] = distanciaAtual[vizinho]

        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1]) #seleciona o menor vizinho
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print(distanciaAtual)

TotalCidades = int(input("Diga quantas cidades existem em volta: "))
TotalVoos = int(input("Diga quantos voos são possíveis de fazer: "))

distancias = {}
for i in range(TotalVoos):
	print()
	Cidade1 = str(input("Informe a primeira cidade: "))
	Cidade2 = str(input("Informe a segunda cidade: "))
	DistanciaVoo = int(input("Informe a distancia entre essas cidades: "))
	if i == 0:
		CidadeOrigem = (Cidade1,Cidade2)
	distancias[Cidade1,Cidade2] = DistanciaVoo

dijkstra(distancias,CidadeOrigem)
