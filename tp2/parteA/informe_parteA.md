## Ejercicio 1

### Consigna

Dos Agentes secretos intentan hacerse con unos informes clasificados. El espía 1 - que es el que los tiene - se encuentra en un punto de la ciudad escondido y tiene que ir al aeropuerto. El espía 2 se encuentra en otro punto de la ciudad y desea interceptarlo. Para eso tiene que llegar al aeropuerto antes que su rival y emboscarlo.

Dado un mapa de una ciudad, las ubicaciones de los espías y el aeropuerto determine quién se quedará con los informes.
Repita el procedimiento pero introduciendo costos en los caminos.
Analice la complejidad añadida si se solicita retornar el camino realizado por cada espía en los pasos 1 y 2.
Realiza los pasos 1 y 2 nuevamente retornando como salida de ejecución los caminos realizados por cada espía.
El mapa de la ciudad:

El mapa de la ciudad y sus caminos esta representados por un grafo que se almacena en un archivo con formato texto.
Cada vértice del grafo está representado por 2 coordenadas: x e y. Estas coordenadas solo toman valores numéricos enteros y positivos.
Las conexiones entre los puntos del grafo se almacenan una por línea del archivo “mapa.coords” de la forma:

p1.x p1.y - p2.x p2.y

Ejemplo:

```
10 3 - 6 5
4 134 - 9 100
```

Para el punto 1 considere simplemente la cantidad de puntos del mapa recorridos como la distancia
Para el punto 2, el costo de cada camino está dado por la distancia euclídea de cada tramo.
Adicionalmente el programa recibirá por línea de comandos las posiciones del espía 1, 2 y el aeropuerto que deberán ser alguno de los puntos del mapa (se ingresaran cada uno como un numero entero positivo equivalente a la posición en el archivo del mapa de un punto del grafo).

Los programas deben funcionar para cualquier mapa de ciudad. Los algoritmos deben ser eficientes y adecuados al tipo de problema.

### Algoritmo de resolución

Se aplica un algoritmo de Dijkstra con cola de prioridad

TP2-1.py

```
from Grafo import make_grafo

grafo = None
grafo = make_grafo("mapa.coords")
grafo.parsearArchivo()
# grafo.mostrar_grafo()
# _set = list(grafo.devolver_nodos())

# print (_set[0].mostrar() + " es conectado con " + _set[1].mostrar() + ":" + str(grafo.estan_conectados(_set[0], _set[1])))
# print (_set[0].mostrar() + " es conectado con " + _set[2].mostrar() + ":" + str(grafo.estan_conectados(_set[0], _set[2])))
# print (_set[0].mostrar() + " es conectado con " + _set[3].mostrar() + ":" + str(grafo.estan_conectados(_set[0], _set[3])))

# print ('distancia entre ' + _set[0].mostrar() + " y " + _set[1].mostrar())
# print (str(_set[0].distancia_euclidea(_set[1])))

# print ('----------')

grafo.ubicar_espia_1(6, 5)
print('Espia 1 ubicado en (6,5)')
grafo.ubicar_espia_2(10, 3)
print('Espia 2 ubicado en (10,3)')
grafo.ubicar_aeropuerto(9, 100)
print('Aeropuerto ubicado en (9,100)')
print('-----------------------------')
print(grafo.obtener_ganador(True))
# print(grafo.obtener_ganador_euclideo())

```
maps.coord

```
10 3 - 6 5
6 5 - 5 4
5 4 - 4 134
10 3 - 4 134
4 134 - 5 34
5 34 - 9 100
```

Grafo.py

```
import sys
import heapq
from Nodo import make_nodo

class Grafo:
    nodos = None
    espia_1 = None
    espia_2 = None
    aeropuerto = None
    conexiones = {}
    nombre_archivo = ""
    INFINITO = sys.maxsize

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.nodos = set()

    def parsearArchivo(self):
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo.readlines():
                if linea.endswith("\n"):
                    linea = linea[:-1]
                if len(linea) == 0:
                    continue
                partes = linea.split("-")

                nodo1 = None
                for p in partes:
                    # hago esto por cada nodo de la relacion
                    _nodos = p.split(" ")
                    coordenadas = []
                    for _nodo in _nodos:
                        try:
                            if _nodo == '':
                                continue
                            coordenadas.append(int(_nodo))
                        except:
                            pass
                    __nodo = make_nodo(coordenadas[0], coordenadas[1])
                    self.nodos.add(__nodo)
                    if nodo1 == None:
                        nodo1 = __nodo

                conexiones_nodo1 = list()
                if nodo1 in self.conexiones.keys():
                    conexiones_nodo1 = self.conexiones[nodo1]

                conexiones_nodo1.append(__nodo)
                # actualizo
                self.conexiones[nodo1] = conexiones_nodo1

    def mostrar_grafo(self):
        for nodo in self.nodos:
            print('Conexiones de nodo ' + nodo.mostrar() + ':')
            if nodo in self.conexiones.keys():
                adyacentes = self.conexiones[nodo]
                for _con in adyacentes:
                    print(_con.mostrar())

    def devolver_nodos(self):
        return self.nodos

    def ubicar_nodo(self, x, y):
        for _nodo in list(self.nodos):
            if _nodo.x == x and _nodo.y == y:
                return _nodo
        return None

    def ubicar_espia_1(self, x, y):
        espia_1 = self.ubicar_nodo(x, y)
        if espia_1 is not None:
            self.espia_1 = espia_1

    def ubicar_espia_2(self, x, y):
        espia_2 = self.ubicar_nodo(x, y)
        if espia_2 is not None:
            self.espia_2 = espia_2

    def ubicar_aeropuerto(self, x, y):
        aeropuerto = self.ubicar_nodo(x, y)
        if aeropuerto is not None:
            self.aeropuerto = aeropuerto

    def camino_minimo(self, nodo, distancia_euclidea):
        vertices = list(self.nodos)
        visto = {}
        distancia = {}
        padre = {}
        heap = []

        for v in vertices:
            distancia[v] = self.INFINITO
            visto[v] = False
            padre[v] = None

        distancia[nodo] = 0
        heapq.heappush(heap, (nodo, distancia[nodo]))
        while len(heap):
            (u, dist) = heapq.heappop(heap)
            visto[u] = True

            if u in self.conexiones.keys():
                adyacencias = self.conexiones[u]
                for _n in adyacencias:
                    if distancia_euclidea:
                        if distancia[_n] > distancia[u] + u.distancia_euclidea(_n):
                            distancia[_n] = distancia[u] + u.distancia_euclidea(_n)
                            padre[_n] = u
                            heapq.heappush(heap, (_n, distancia[_n]))
                    else:
                        if distancia[_n] > distancia[u] + u.distancia(_n):
                            distancia[_n] = distancia[u] + u.distancia(_n)
                            padre[_n] = u
                            heapq.heappush(heap, (_n, distancia[_n]))
                            print('Desde nodo ' + u.mostrar() + ' paso por ' + _n.mostrar())

        for dist in distancia.keys():
            distancia_str = ' infinito'
            if distancia[dist] != self.INFINITO:
                distancia_str = str(distancia[dist])
            print('distancia de ' + nodo.mostrar() + ' a ' + dist.mostrar() + ':' + distancia_str)

        return distancia, padre

    def reconstruir_camino(self, diccionario, inicial):
        lista = []
        lista.append(inicial)
        nodo_iterador = inicial
        while diccionario[nodo_iterador] is not None:
            lista.append(diccionario[nodo_iterador])
            nodo_iterador = diccionario[nodo_iterador]
        return lista

    def distancia_espia1_aeropuerto(self, euclidea):
        (dist, padre) = self.camino_minimo(self.espia_1, euclidea)
        camino = self.reconstruir_camino(padre, self.aeropuerto)
        return (dist[self.aeropuerto], camino)

    def distancia_espia2_aeropuerto(self, euclidea):
        (dist, padre) = self.camino_minimo(self.espia_2, euclidea)
        camino = self.reconstruir_camino(padre, self.aeropuerto)
        return (dist[self.aeropuerto], camino)

    def obtener_ganador(self, euclidea = False):
        (distancia_espia1, camino_espia1) = self.distancia_espia1_aeropuerto(euclidea)
        (distancia_espia2, camino_espia2) = self.distancia_espia2_aeropuerto(euclidea)
        if distancia_espia1 < distancia_espia2:
            ganador = "El ganador es el espia 1"
            ruta_ganadora = camino_espia1
        else:
            ganador = "El ganador es el espia 2"
            ruta_ganadora = camino_espia2

        _recorrido = ""
        for _nodo in ruta_ganadora:
            _recorrido = _recorrido + ' ' + _nodo.mostrar()
        return ganador + " y la ruta que recorrio fue" + _recorrido

def make_grafo(archivo):
    grafo = Grafo(archivo)
    return grafo
```


### Resolución


```
Espia 1 ubicado en (6,5)
Espia 2 ubicado en (10,3)
Aeropuerto ubicado en (9,100)
-----------------------------
distancia de (6,5) a (4,134):131.41805965932517
distancia de (6,5) a (9,100):297.5441605535976
distancia de (6,5) a (5,4):1.4142135623730951
distancia de (6,5) a (10,3): infinito
distancia de (6,5) a (5,34):231.4230595343314
distancia de (6,5) a (6,5):0
distancia de (10,3) a (4,134):131.13733259449805
distancia de (10,3) a (9,100):297.2634334887705
distancia de (10,3) a (5,4):5.8863495173726745
distancia de (10,3) a (10,3):0
distancia de (10,3) a (5,34):231.1423324695043
distancia de (10,3) a (6,5):4.47213595499958
El ganador es el espia 2 y la ruta que recorrio fue (9,100) (5,34) (4,134) (10,3)
```


