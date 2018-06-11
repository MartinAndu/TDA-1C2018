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

    def agregar_arista(self, u, v):
        if u < v:
            self.aristas.add((u,v))
        else:
            self.aristas.add((v, u))

    def existe_arista(self, u, v):
        clave = None
        if u < v:
            clave = (u,v)
        else:
            clave = (v, u)

        return clave in self.aristas

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

                # self.ubicar_capacidades(self.capacidades,nodo_origen, nodo_destino, capacidad)
                self.capacidades[(nodo_origen, nodo_destino)] = capacidad

                # agrego a las conexiones
                conexiones_nodo1 = list()
                conexiones_nodo = list()

                if nodo_origen in self.conexiones.keys():
                    conexiones_nodo1 = self.conexiones[nodo_origen]
                if nodo_destino in self.conexiones.keys():
                    conexiones_nodo = self.conexiones[nodo_destino]

                conexiones_nodo1.append(nodo_destino)
                conexiones_nodo.append(nodo_origen)
                self.conexiones[nodo_origen] = conexiones_nodo1
                self.conexiones[nodo_destino] = conexiones_nodo

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

    def bfs(self, s, t, padre):
        ''' Devuelve true si existe un camino entre s y t,
            en el parametro padre devuelve desde donde se
            llego
        '''
        cola = collections.deque()
        visitados = {}

        for v in self.vertices:
            visitados[v] = False

        cola.append(s)
        visitados[s] = True

        while len(cola) > 0:
            u = cola.popleft()
            ady = self.conexiones[u]
            if ady is None:
                continue

            for v in ady:
                if (visitados[v] == False) and (self.grafo_residual[(u, v)] > 0):
                    cola.append(v)
                    padre[v] = u
                    visitados[v] = True

        return visitados[t]

    def obtener_flujo_maximo(self):
        return self.flujo_maximo(self.fuente, self.sumidero)

    def flujo_maximo(self, fuente, sumidero):
        padre = {}
        for v in self.vertices:
            padre[v] = None

        maximo_flujo = 0

        for v in self.conexiones.keys():
            ady = self.conexiones[v]
            if ady is not None:
                for u in ady:
                    if (u, v) in self.capacidades.keys():
                        self.grafo_residual[(u,v)] = self.capacidades[(u, v)]
                        self.grafo_residual[(v, u)] = self.capacidades[(u, v)]
                    else:
                        self.grafo_residual[(u, v)] = self.capacidades[(v, u)]
                        self.grafo_residual[(v, u)] = self.capacidades[(v, u)]

        while self.bfs(fuente, sumidero, padre):
            c_f = float("Inf")
            s = sumidero

            while s != fuente:
                c = self.grafo_residual[(padre[s], s)]
                # tomo el minimo
                c_f = min( c_f, c)
                s = padre[s]

            maximo_flujo += c_f

            v = sumidero
            while v != fuente:
                u = padre[v]
                self.grafo_residual[(u, v)] -= c_f
                self.grafo_residual[(v, u)] += c_f
                v = padre[v]

        flujos_ordenados = sorted(self.grafo_residual.items(), key=operator.itemgetter(1))
        return maximo_flujo
