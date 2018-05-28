from Grafo import make_grafo
import sys, getopt

def main():
    grafo = None
    euclidea = False
    inputfile = input('Ingrese la ruta del mapa: ')
    entrada_valida = False

    while not entrada_valida:
        euclidea = input('Usar distancia euclidea: (S/N)')
        if euclidea == 'S' or euclidea == 's':
            euclidea = True
            entrada_valida = True
        elif euclidea == 'N' or euclidea == 'n':
            euclidea = False
            entrada_valida = True
        else:
            print('Debe ingresar S o N')

    try:
        grafo = make_grafo(inputfile)
        grafo.parsearArchivo()
    except:
        print('Error al procesar el archivo')
        sys.exit(2)

    print('Ingrese ubicacion del espia 1:')
    x1 = input('Ingrese coordenada x: ')
    y1 = input('Ingrese coordenada y: ')

    grafo.ubicar_espia_1(int(x1), int(y1))
    print('Espia 1 ubicado en (' + x1 + ',' + y1 + ')')
    print('Ingrese ubicacion del espia 2:')
    x1 = input('Ingrese coordenada x: ')
    y1 = input('Ingrese coordenada y: ')

    grafo.ubicar_espia_2(int(x1), int(y1))
    print('Espia 2 ubicado en (' + x1 + ',' + y1 + ')')
    print('Ingrese ubicacion del aeropuerto:')
    x1 = input('Ingrese coordenada x: ')
    y1 = input('Ingrese coordenada y: ')
    grafo.ubicar_aeropuerto(int(x1), int(y1))
    print('Aeropuerto ubicado en (' + x1 + ',' + y1 + ')')
    print('-----------------------------')
    print(grafo.obtener_ganador(euclidea))

if __name__ == "__main__":
    main()
