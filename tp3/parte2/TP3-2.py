from Grafo1 import Grafo

g = Grafo('redsecreta1.map')
n = 2
g.parsear_archivo()
print(g.obtener_flujo_maximo())

#lista = g.devolver_minimos(n)
#salida = ""
#for e in lista:
#    salida += str(e)
#print('Ubicaria ' + str(n) + ' personas a vigilar las aristas: ' + salida)