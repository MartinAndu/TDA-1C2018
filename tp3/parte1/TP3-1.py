
import sys

from batalla_naval import Juego, NaiveLanzaderos
from estrategia_greedy import EstrategiaGreedy
from estrategia_dinamico import EstrategiaDinamico


def print_error():
    print('Por favor, ejecute el juego de la siguiente forma:', '',
          'python TP3-1.py <tablero> <lanzaderas> <estrategia>', sep='\n')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print_error()
        exit(1)
    else:
        tablero = sys.argv[1]
        lanzaderas = int(sys.argv[2])
        try:
            estrategia = {
                'naive': NaiveLanzaderos,
                'greedy': EstrategiaGreedy,
                'dinamico': EstrategiaDinamico
            }[sys.argv[3]]
        except KeyError:
            print('Estrategia debe ser "naive", "greedy" o "dinamico"')
        estrategia = estrategia()
        try:
            Juego(tablero_file=tablero, lanzaderos=lanzaderas,
                  estrategia=estrategia).jugar()
        except FileNotFoundError:
            print('Especifique una ruta al archivo tablero válida!')
