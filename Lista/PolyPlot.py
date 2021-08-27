import numpy
from matplotlib import pyplot

# objective function
def PolyCoefficients(x, coeffs):
	o = len(coeffs)
	teste = o
	y = 0
	
	for i in range(o):
		y += coeffs[i]*x**(teste)
		teste -= 1

	return y

x = numpy.linspace(-1.5, 3, 100)
coeffs = [2,-13,26,-7,-28,20]

axes = pyplot.gca()
axes.set_ylim([-20, 20])

pyplot.plot(x, PolyCoefficients(x, coeffs))

#optima
x_optima = 0.0

pyplot.axvline(x=x_optima, ls='--', color='red')
pyplot.axhline(y=x_optima, ls='--', color='red')

#show the plot
pyplot.show()
