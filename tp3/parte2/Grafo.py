import collections
import operator

class Grafo:
    capacidades = {}
    grafo_residual = {}
    vertices = None

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.vertices = set()
        self.capacidades = {}
        self.conexiones = {}

    def parsear_archivo(self):
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo.readlines():
                if linea.endswith("\n"):
                    linea = linea[:-1]
                if len(linea) == 0:
                    continue
                partes = linea.split(" ")
                nodo_origen = int(partes[0])

                nodo_destino = int(partes[1])
                capacidad = int(partes[2])

                self.capacidades[(nodo_origen, nodo_destino)] = capacidad

                # agrego a las conexiones
                conexiones_nodo1 = set()
                conexiones_nodo = set()

                if nodo_origen in self.conexiones.keys():
                    conexiones_nodo1 = self.conexiones[nodo_origen]

                conexiones_nodo1.add(nodo_destino)

                self.conexiones[nodo_origen] = conexiones_nodo1
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
        
        self.conexiones[1] = None

    def reconstruir_camino(self, diccionario, inicial):
        lista = []
        lista.append(inicial)
        nodo_iterador = inicial
        while diccionario[nodo_iterador] is not None:
            lista.append(diccionario[nodo_iterador])
            nodo_iterador = diccionario[nodo_iterador]
        return lista

    def bfs(self, s, t, padre):
        ''' Devuelve true si existe un camino entre s y t,
            en el parametro padre devuelve desde donde se
            llego
        '''
        for v in self.vertices:
            padre[v] = None
        cola = collections.deque()
        visitados = {}

        for v in self.vertices:
            visitados[v] = False

        cola.append(s)
        visitados[s] = True

        while len(cola) > 0:
            u = cola.pop()
            ady = self.conexiones[u]
            if ady is None:
                continue
        
            for v in ady:
                if (visitados[v] == False) and self.grafo_residual[(u,v)] > 0:
                    cola.append(v)
                    padre[v] = u
                    visitados[v] = True
        print(self.reconstruir_camino(padre, 1))
        return visitados[t]

    def quitar_arista(self, arista):
        del self.capacidades[arista]
        v1 = arista[0]
        v2 = arista[1]

        _set = self.conexiones[v1]
        _set.remove(v2)

                
    def obtener_flujo_maximo(self):
        return self.flujo_maximo(self.fuente, self.sumidero)

    def flujo_maximo(self, fuente, sumidero):
        padre = {}
        flujo_maximo_arista = {}
        maximo_flujo = 0
        self.grafo_residual.clear()
        
        for v in self.conexiones.keys():
            ady = self.conexiones[v]
            if ady is not None:
                for u in ady:
                    if (u, v) in self.capacidades.keys():
                        self.grafo_residual[(u,v)] = self.capacidades[(u, v)]
                        self.grafo_residual[(v, u)] = 0
                    elif (v, u) in self.capacidades.keys():
                        self.grafo_residual[(v, u)] = self.capacidades[(v, u)]
                        self.grafo_residual[(u, v)] = 0

        while self.bfs(fuente, sumidero, padre):
            c_f = float("Inf")
            s = sumidero

            while s != fuente:
                c = self.capacidades[(padre[s], s)]
                # tomo el minimo
                c_f = min( c_f, c)
                s = padre[s]

            maximo_flujo += c_f

            v = sumidero
            while v != fuente:
                u = padre[v]
                self.grafo_residual[(u, v)] -= c_f                
                self.grafo_residual[(v, u)] += c_f
                flujo_maximo_arista[(v,u)] = self.grafo_residual[(v, u)]
                v = padre[v]

        flujos_ordenados = sorted(flujo_maximo_arista.items(), key=operator.itemgetter(1), reverse=True)
        return (flujos_ordenados[0][0][1], flujos_ordenados[0][0][0])
