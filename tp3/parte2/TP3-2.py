
import sys

from Grafo import Grafo


def print_error():
    print('Por favor, ejecute el juego de la siguiente forma:', '',
          'python TP3-2.py <archivo de red>', sep='\n')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_error()
        exit(1)
    else:
        g = Grafo(sys.argv[1])
        n = 2
        try:
            g.parsear_archivo()
        except FileNotFoundError:
            print('Especifique una ruta al archivo de red válida!')
            exit(1)
        for i in range(n):
            arista_maxima = g.obtener_flujo_maximo()
            print('Colocaria un vigilador en la arista ' + str(arista_maxima))
            g.quitar_arista(arista_maxima)
