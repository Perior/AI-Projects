import numpy as np
from numpy.random import randn
from numpy.random import rand
from numpy.core._asarray import asarray
from numpy.random.mtrand import seed
from matplotlib import pyplot as plt
import itertools
from math import exp

#Resolve o polinomio de grau 6
def polycoeffs(x, coeffs):
	o = len(coeffs)
	teste = o
	y = 0
	
	for i in range(o):
		y += coeffs[i]*x**(teste)
		teste -= 1

	return y


def simulatedannealing(polycoeffs, coeffs, bounds, n_iteracoes, passo, temp):
    #Inicializa o programa em um ponto aleatório do gráfico
    inicial = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    aval_inicial = polycoeffs(inicial, coeffs)

    atual, aval_atual = inicial, aval_inicial

    #Armazena os resultados das funções em uma lista
    resultados = list()
    resultados.append(inicial)

    print('>0 f(%s) = %.5f' % (inicial, aval_inicial))

    for i in range(n_iteracoes):
        candidato = atual + randn(len(bounds)) * passo
        aval_candidato = polycoeffs(candidato, coeffs)
        #Avalia se o estado do passo aleatório é menor (melhor) que o estado anterior
        if(aval_candidato < aval_inicial):
            inicial, aval_inicial = candidato, aval_candidato
            resultados.append(inicial)
            print('>%d f(%s) = %.5f' % (i, inicial, aval_inicial))

        delta = aval_candidato - aval_atual
        t = temp / float(i + 1)
        probabilidade = exp(-delta/t)

        if (delta < 0 or rand() <  probabilidade):
            atual, aval_atual = candidato, aval_candidato

    return [inicial, aval_inicial, resultados]


#Limites do gráfico da função
bounds = asarray([[-1.5, 3.0]])
n_iteracoes = 2000
#Operador que altera os intervalos de busca no gráfico.
passo = 0.1
coeffs = [2,-13,26,-7,-28,20]
temp = 100

x = np.linspace(-1.5, 3, 100)
axes = plt.gca()
axes.set_ylim([-20, 20])

plt.plot(x, polycoeffs(x, coeffs))

plt.axvline(x=0.0, ls='--', color='red')
plt.axhline(y=0.0, ls='--', color='red')

colors = itertools.cycle(["m", "b", "g", "c"])

#Número de inicializações: 4
for i in range(4):
    melhor, score, resultados = simulatedannealing(polycoeffs, coeffs, bounds, n_iteracoes, passo, temp)
    print("\n")
    plt.plot(resultados, [polycoeffs(x, coeffs) for x in resultados], 'o', color = next(colors))
    plt.plot([resultados.pop(-1)] ,[polycoeffs(resultados.pop(-1), coeffs)], 'o', color = 'red')

plt.show()