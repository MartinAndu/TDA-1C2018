import sys
import heapq
import operator

class Grafo:
    vertices = None
    fuente = None
    sumidero = None
    conexiones = {}
    nombre_archivo = ""

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.vertices = set()
        self.capacidades = {}


    def parsearArchivo(self):
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo.readlines():
                if linea.endswith("\n"):
                    linea = linea[:-1]
                if len(linea) == 0:
                    continue
                partes = linea.split(" ")
                conexiones_nodo = list()
                nodo_origen = int(partes[0])

                if nodo_origen in self.conexiones.keys():
                    conexiones_nodo = self.conexiones[nodo_origen]

                nodo_destino = int(partes[1])
                capacidad = int(partes[2])

                # self.ubicar_capacidades(self.capacidades,nodo_origen, nodo_destino, capacidad)
                self.capacidades[(nodo_origen, nodo_destino)] = capacidad
                conexiones_nodo.append(nodo_destino)
                self.conexiones[nodo_origen] = conexiones_nodo

                # agrego los vertices al conjunto de vertices totales
                self.vertices.add(nodo_origen)
                self.vertices.add(nodo_destino)

                if nodo_origen == 0:
                    self.fuente = nodo_origen
                elif nodo_destino == 0:
                    self.fuente = nodo_destino
                elif nodo_origen == 1:
                    self.sumidero = nodo_origen
                elif nodo_destino == 1:
                    self.sumidero = nodo_destino
        self.conexiones[self.sumidero] = None

    def devolver_nodos(self):
        return self.vertices

    def buscar_capacidad(self, diccionario, u, v):
        if u < v:
            return diccionario[(u,v)]
        return diccionario[(v, u)]

    def ubicar_capacidades(self, diccionario, u, v, capacidad):
        if u < v:
            diccionario[(u,v)] = capacidad
        else:
            diccionario[(v, u)] = capacidad

    def calcular_flujo_maximo(self):
        flujos = {}
        G_t = self.capacidades

        for v in self.conexiones.keys():
            ady = self.conexiones[v]
            if ady is not None:
                for u in ady:
                    #flujos[(u,v)] = 0
                    flujos[(v, u)] = 0
        anterior = None
        # tengo que construir G*
        for v in self.conexiones.keys():
            ady = self.conexiones[v]
            capacidades_aristas_ady = list()
            if ady is not None:
                for u in ady:
                    capacidades_aristas_ady.append(self.capacidades[(v, u)])

                capacidades_aristas_ady.sort()
                # tomo el minimo
                c_f = capacidades_aristas_ady[0]
                for u in ady:
                    flujos[(v, u)] = self.capacidades[(v, u)] - c_f
                    #flujos[(u, v)] = - flujos[(v, u)]

        flujos_ordenados = sorted(flujos.items(), key=operator.itemgetter(1))
        return flujos_ordenados

    def devolver_minimos(self, n):
        flujos = self.calcular_flujo_maximo()
        lista = list()
        for i in range(n):
            lista.append(flujos[i][0])
        return lista

def make_grafo(archivo):
    grafo = Grafo(archivo)
    return grafo
