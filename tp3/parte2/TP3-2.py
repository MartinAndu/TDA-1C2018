from Grafo1 import Grafo

g = Grafo('redsecreta2.map')
n = 2
g.parsear_archivo()
for i in range(n):
    arista_maxima = g.obtener_flujo_maximo()
    print('Colocaria un vigilador en la arista ' + str(arista_maxima))
    g.quitar_arista(arista_maxima)