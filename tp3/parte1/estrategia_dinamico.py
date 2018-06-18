
from batalla_naval import Estrategia, Juego

from itertools import combinations


def copiar_barcos(barcos):
    return {k: v.copy() for k, v in barcos.items()}


def mover_barcos(barcos, tablero):
    for barco in barcos:
        barcos[barco]['posicion'] += 1
        if barcos[barco]['posicion'] >= len(tablero[barco]):
            barcos[barco]['posicion'] = 0


def posibles_disparos(barcos, m):
    rs = []
    for k in barcos:
        rs.extend([k] * m)
    return set(combinations(rs, m))


def disparos_optimos(disparos, barcos, tablero):
    for d in disparos:
        if barcos[d]['vida'] <= 0:
            # Si alguno de los disparos va a un barco sin vida, corto, porque
            # seguro hay un set de disparos mejor
            return False
    return True


def resultado_de_disparos(disparos, barcos, tablero):
    vida_actual = {b: v['vida'] for b, v in barcos.items()}
    danio_total = 0
    for d in disparos:
        danio_posible = tablero[d][barcos[d]['posicion']]
        danio_total += max(min(danio_posible, vida_actual[d]), 0)
        vida_actual[d] -= danio_posible
    return len([x for x in vida_actual.values() if x > 0]), danio_total


def resolver_turno(disparos, barcos, tablero):
    for d in disparos:
        barcos[d]['vida'] -= tablero[d][barcos[d]['posicion']]
    mover_barcos(barcos, tablero)


def obtener_posicion(barcos, tablero):
    s = []
    for i in sorted(barcos):
        barco = barcos[i]
        vida = max(barco['vida'], 0)
        s.append(str(vida) + 'v' + str(tablero[i][barco['posicion']]) + 'p')
    return '|'.join(s)


class EstrategiaDinamico(Estrategia):

    m = None
    res = None

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.callcount = 0

    def optimo_recursivo(self, posicion, disparos_hechos, disparos_posibles,
                         tablero, barcos):

        if posicion not in self.m:
            self.m[posicion] = {}
        if disparos_hechos in self.m[posicion]:
            return self.m[posicion][disparos_hechos]

        self.callcount += 1
        if self.callcount > 3000000:
            print(posicion)
            raise Exception('El tablero es demasiado grande para mi =(')

        tablero = tablero.copy()
        barcos = copiar_barcos(barcos)
        maximo = float('inf')
        p, danio = resultado_de_disparos(disparos_hechos, barcos, tablero)
        if danio == 0:
            return maximo
        pos = self.m[posicion]
        if p == 0:
            pos[disparos_hechos] = p
            self.res[posicion] = disparos_hechos
            return p
        else:
            resolver_turno(disparos_hechos, barcos, tablero)
            nueva_posicion = obtener_posicion(barcos, tablero)
            pos[disparos_hechos] = maximo
            for disparos in disparos_posibles:
                if not disparos_optimos(disparos, barcos, tablero):
                    continue
                k = self.optimo_recursivo(nueva_posicion, disparos, disparos_posibles,
                                          tablero, barcos)

                if p + k < pos[disparos_hechos]:
                    pos[disparos_hechos] = p + k
                    self.res[nueva_posicion] = disparos
                    if k == 0:
                        break
        return self.m[posicion][disparos_hechos]

    def construir_matriz(self, tablero, lanzaderos, barcos):
        self.m = {}
        self.res = {}

        disparos_posibles = posibles_disparos(barcos, lanzaderos)
        if self.verbose:
            print('disparos posibles: ', disparos_posibles)

        minimo = float('inf')
        posicion_inicial = obtener_posicion(barcos, tablero)
        for disparos in disparos_posibles:
            k = self.optimo_recursivo(posicion_inicial, disparos, disparos_posibles, tablero, barcos)
            if k < minimo:
                minimo = k
                self.res[posicion_inicial] = disparos

    def siguiente_turno(self, tablero, lanzaderos, barcos, turno):
        if not self.res:
            self.construir_matriz(tablero, lanzaderos, barcos)
            print('Dinámico: tamaño de la matriz', len(self.res))

        posicion = obtener_posicion(barcos, tablero)
        disparos = self.res[posicion]
        if self.verbose:
            print('Estrategia dinamica para turno: ', turno, ', disparos: ', disparos,
                  ', minimo recursivo: ', self.m[turno][disparos])
        return disparos


if __name__ == '__main__':
    estrategia = EstrategiaDinamico(verbose=False)
    Juego(tablero_file='tablero3', lanzaderos=3,
          estrategia=estrategia).jugar()
