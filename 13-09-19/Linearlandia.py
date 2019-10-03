# 2 <= qtde. de Municipios <= 10000
# 1 <= Partida/Chegada <= qtde. de Municipios
# 1 <= Distancia <= 100

from random import randint
Linearlandia = {}
Municipios = int(input("digite a quantidade de Municipios: "))
Partida = int(input("digite o ponto de partida: "))
Chegada = int(input("digite o ponto de chegada: "))

if Partida > Municipios or Chegada > Municipios:
    print("o ponto de Partida/Chegada não corresponde")

cont = 0
DistanciaTotal = 0
while cont != Municipios:
    d = {}
    ProxCidade = randint(1,Municipios)
    Estrada = randint(1,100)
    if ProxCidade in Linearlandia:
        continue
    elif cont == 0:
        ProxCidade = Partida
    elif cont == Municipios-1:
        ProxCidade = Chegada
    d[ProxCidade] = Estrada
    Linearlandia.update(d)
    DistanciaTotal += Estrada
    cont += 1

print(DistanciaTotal)
