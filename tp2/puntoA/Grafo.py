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

    def camino_minimo(self, nodo, distancia=1):
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
                    if distancia == 1:
                        if distancia[_n] > distancia[u] + u.distancia_euclidea(_n):
                            distancia[_n] = distancia[u] + u.distancia_euclidea(_n)
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

    def distancia_euclidea_espia1_aeropuerto(self):
        (dist, padre) = self.camino_minimo(self.espia_1)
        camino = self.reconstruir_camino(padre)
        return dist[self.aeropuerto]

    def distancia_euclidea_espia2_aeropuerto(self):
        (dist, padre) = self.camino_minimo(self.espia_2)
        return dist[self.aeropuerto]

    def distancia_espia1_aeropuerto(self):
        (dist, padre) = self.camino_minimo(self.espia_1, 2)
        camino = self.reconstruir_camino(padre, self.aeropuerto)
        return (dist[self.aeropuerto], camino)

    def distancia_espia2_aeropuerto(self):
        (dist, padre) = self.camino_minimo(self.espia_2, 2)
        camino = self.reconstruir_camino(padre, self.aeropuerto)
        return (dist[self.aeropuerto], camino)

    def obtener_ganador(self):
        (distancia_espia1, camino_espia1) = self.distancia_espia1_aeropuerto()
        (distancia_espia2, camino_espia2) = self.distancia_espia2_aeropuerto()
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

    def obtener_ganador_euclideo(self):
        if self.distancia_euclidea_espia1_aeropuerto() < self.distancia_euclidea_espia2_aeropuerto():
            return "El ganador es el espia 1"
        else:
            return "El ganador es el espia 2"


def make_grafo(archivo):
    grafo = Grafo(archivo)
    return grafo