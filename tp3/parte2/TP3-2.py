from Grafo import Grafo

g = Grafo('redsecreta.map')
n = 2
g.parsearArchivo()
lista = g.devolver_minimos(n)
salida = ""
for e in lista:
    salida += str(e)
print('Ubicaria ' + str(n) + ' personas a vigilar las aristas: ' + salida)