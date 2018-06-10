

class Estrategia:
    """ Clase base para las estrategias. """

    def siguiente_turno(self, tablero, lanzaderos, barcos, turno):
        """
        Este método debe ejecutar un turno, basandose en los datos del tablero,
        lanzaderos y barcos actuales.

        Parametros:

        - tablero es un diccionario que tiene como clave el número de línea (o
          número de barco, que es lo mismo) y como valores una lista con las
          los números de daño de cada celda. Por ejemplo:

          {1: [10, 20, 30, 10]}

        - lanzaderos es el número de lanzaderos

        - barcos es un diccionario que tiene como claves números de barco, y
          como valores un diccionario con sus puntos de vida y su posición en el
          tablero. Por ejemplo:

          {1: {'vida': 50, 'posicion': 0}}

        - turno es el número del turno a hacer

        Este método tiene que devolver una lista con los números de
        barcos a los que disparar (el tamaño de la lista debe ser igual a la
        cantidad de lanzaderos)
        """
        pass


class NaiveLanzaderos(Estrategia):

    def siguiente_turno(self, tablero, lanzaderos, barcos, turno):
        """
        Estrategia naive que dispara todos los misiles al primer barco con vida
        que encuentra
        """
        for i, barco in barcos.items():
            if barco['vida'] > 0:
                return [i] * lanzaderos


class Juego:

    def __init__(self, tablero_file, lanzaderos, estrategia):
        self.tablero_file = tablero_file
        self.tablero = {}
        self.lanzaderos = lanzaderos
        self.barcos = {}
        self.estrategia = estrategia

    def parsear_tablero(self):
        with open(self.tablero_file) as f:
            for i, line in enumerate(f):
                splits = list(map(int, line.split()))
                self.barcos[i] = {
                    'posicion': 0,
                    'vida': splits[0]
                }
                self.tablero[i] = splits[1:]

    def cantidad_barcos_vivos(self):
        return len([x for x in self.barcos.values() if x['vida'] > 0])

    def mover_barco(self, barco):
        self.barcos[barco]['posicion'] += 1
        if self.barcos[barco]['posicion'] >= len(self.tablero[barco]):
            self.barcos[barco]['posicion'] = 0

    def mover_barcos(self):
        for barco in self.barcos:
            self.mover_barco(barco)

    def disparar_misiles(self, misiles):
        for misil in misiles:
            barco = self.barcos[misil]
            danio = self.tablero[misil][barco['posicion']]
            self.barcos[misil]['vida'] -= danio

    def imprimir_turno(self, turno, puntos):
        print('Turno actual: {}, puntos acumulados: {}. Barcos disponibles:'
              .format(turno, puntos))
        for i, barco in self.barcos.items():
            if barco['vida'] > 0:
                pos = barco['posicion']
                print('Barco {}. Vida: {}, posición: {}, daño potencial: {}'
                      .format(i, barco['vida'], pos, self.tablero[i][pos]))
        print('-' * 40)

    def imprimir_misiles(self, misiles_disparados):
        msg = 'Lanzadero {} al barco {} (-{} de vida)'
        mensajes = [msg.format(i, k, self.tablero[k][self.barcos[k]['posicion']])
                    for i, k in enumerate(misiles_disparados)]
        print('Misiles lanzados: ' + ', '.join(mensajes))
        print('-' * 40)

    def imprimir_final(self, turno, puntos):
        print('Juego finalizado! Cantidad de turnos: {}. Puntos acumulados: {}'
              .format(turno, puntos))

    def jugar(self):
        self.parsear_tablero()
        args = (self.tablero, self.lanzaderos, self.barcos)

        turno = 0
        puntos = 0
        print('Inicio del juego!')
        self.imprimir_turno(turno, puntos)

        while True:
            turno += 1
            print('Comienzo del turno', turno)
            misiles_disparados = self.estrategia.siguiente_turno(*args, turno=turno)
            self.imprimir_misiles(misiles_disparados)
            self.disparar_misiles(misiles_disparados)

            barcos_vivos = self.cantidad_barcos_vivos()
            if barcos_vivos == 0:
                break
            puntos += barcos_vivos

            self.mover_barcos()
            self.imprimir_turno(turno, puntos)

        self.imprimir_final(turno, puntos)


if __name__ == '__main__':
    estrategia = NaiveLanzaderos()
    Juego(tablero_file='tablero', lanzaderos=2,
          estrategia=estrategia).jugar()
