
import matplotlib.pyplot as plt

dados = open('original.csv').readlines()

x = []

y = []


for dado in range(len(dados)):
	if dado != 0:
		linha = dados[dado].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.plot(x,y)
plt.show()



