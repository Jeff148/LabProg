# representação do mapa em Matriz de Adjacência
# a entrada consiste em informar o tamanho do mapa e mostrar pontos que sejam adjacentes
# o objetivo é informar a qtde mínima de cores usadas para colorir um mapa
# pontos adjacentes não podem ser da mesma cor

from random import randint
Mapa = []

Tam = int(input("Digite o tamanho do Mapa: "))

# criação da matriz
for l in range(Tam):
	Linha = []
	for c in range(Tam):
		Linha.append(randint(0,1))
	Mapa.append(Linha)

# arrumando adjacência
n = 0
while n != Tam:
	Mapa[n][n] = 0
	n += 1

for l in range(Tam):
	for c in range(Tam):
		p = Mapa[l][c]
		if p != Mapa[c][l]:
		    Mapa[c][l] = p

# mostra a matriz
for l in range(Tam):
    for c in range(Tam):
        print(Mapa[l][c], end='\t')
    print('')
