# INCOMPLETO
# while L[i] != MaxAltura:
Num = int(input("digite a qtde. de retângulos: "))
MaxAltura = 0
L = []

if Num < 1 or Num > 10**5:
	print("limite de retângulos excedido")

print("digite a Altura dos retângulos")
for i in range(Num):
	Altura = int(input("%dº: " % (i+1)))
	if Altura < 1 or Altura > 10**9:
		continue
	else:
		L.append(Altura)
		if Altura >= MaxAltura:
			MaxAltura = Altura

# função para max. de cortes
def CortePonto(L,vales=1,listagemVales=[]):
	for v in range(MaxAltura):
		for h in range(len(L)):
			if L[h] >= v:
				vales += 1
			if L[h] < v:
				continue
		listagemVales.append(vales)
		vales = 1
	return max(listagemVales)

CortePonto(L,listagemVales=1)
