print("informe o caminho do robô")
print("use F para ir em frente")
print("use T para ir atrás")
print('')

cont = 0
espaco = ''
sequencia = str(input("diga para qual direção o robô vai: "))
tam = len(sequencia)

for r in range(tam):
	if sequencia[r] == 'F':
		cont += 1
	if sequencia[r] == 'T':
		cont -= 1
print("a posicão atual do robô é ", cont)

if cont == 0:
	print("a Posição inicial e atual são as mesmas")
else:
	print("a Posição inicial e atual são diferentes")
