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

                # agrego a las conexiones
                conexiones_nodo1 = list()
                conexiones_nodo = list()

                if nodo1 in self.conexiones.keys():
                    conexiones_nodo1 = self.conexiones[nodo1]
                if __nodo in self.conexiones.keys():
                    conexiones_nodo = self.conexiones[__nodo]

                conexiones_nodo1.append(__nodo)
                conexiones_nodo.append(nodo1)
                self.conexiones[nodo1] = conexiones_nodo1
                self.conexiones[__nodo] = conexiones_nodo

    def devolver_nodos(self):
        return self.nodos

    def ubicar_nodo(self, x, y):
        for _nodo in self.nodos:
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

    def camino_minimo_unitario(self):
        return self.bfs(self.aeropuerto)

    def bfs(self, u):
        nivel = {}
        padre = {}
        cola = list()
        for v in self.nodos:
            nivel[v] = 0
            padre[v] = None

        nivel[u] = 0
        cola.append(u)
        while len(cola) > 0:
            v = cola.pop()
            if nivel[v] == 0:
                if padre[v] is None:
                    nivel[v] = 1
                else:
                    nivel[v] = nivel[padre[v]] + 1
                ady = self.conexiones[v]
                for a in ady:
                    if nivel[a] == 0:
                        cola.append(a)
                        padre[a] = v

        return nivel, padre
    
    def camino_minimo(self, nodo):
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
                    if distancia[_n] > distancia[u] + u.distancia_euclidea(_n):
                        distancia[_n] = distancia[u] + u.distancia_euclidea(_n)
                        padre[_n] = u
                        heapq.heappush(heap, (_n, distancia[_n]))
        return distancia, padre

    def reconstruir_camino(self, diccionario, inicial):
        lista = []
        lista.append(inicial)
        nodo_iterador = inicial
        while diccionario[nodo_iterador] is not None:
            lista.append(diccionario[nodo_iterador])
            nodo_iterador = diccionario[nodo_iterador]
        return lista

    def obtener_ganador(self, euclidea):
        padre = None
        if not euclidea:
            (dist, padre) = self.camino_minimo_unitario()
            distancia_espia1 = dist[self.espia_1]
            distancia_espia2 = dist[self.espia_2]
        else:
            (dist, padre) = self.camino_minimo(self.aeropuerto)
            distancia_espia1 = dist[self.espia_1]
            distancia_espia2 = dist[self.espia_2]

        if distancia_espia1 < distancia_espia2:
            ganador = "El ganador es el espia 1"
            ruta_ganadora = self.reconstruir_camino(padre, self.espia_1)
        else:
            ganador = "El ganador es el espia 2"
            ruta_ganadora = self.reconstruir_camino(padre, self.espia_2)

        _recorrido = ""
        for _nodo in ruta_ganadora:
            _recorrido = _recorrido + ' ' + _nodo.mostrar()
        return ganador + " y la ruta que recorrio fue" + _recorrido

def make_grafo(archivo):
    grafo = Grafo(archivo)
    return grafo
