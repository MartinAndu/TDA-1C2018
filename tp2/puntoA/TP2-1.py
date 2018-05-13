from Grafo import make_grafo

grafo = None
grafo = make_grafo("/mnt/cosas/facu/TDA/TP2/TP2/mapa.coords")
grafo.parsearArchivo()
# grafo.mostrar_grafo()
# _set = list(grafo.devolver_nodos())

# print (_set[0].mostrar() + " es conectado con " + _set[1].mostrar() + ":" + str(grafo.estan_conectados(_set[0], _set[1])))
# print (_set[0].mostrar() + " es conectado con " + _set[2].mostrar() + ":" + str(grafo.estan_conectados(_set[0], _set[2])))
# print (_set[0].mostrar() + " es conectado con " + _set[3].mostrar() + ":" + str(grafo.estan_conectados(_set[0], _set[3])))

# print ('distancia entre ' + _set[0].mostrar() + " y " + _set[1].mostrar())
# print (str(_set[0].distancia_euclidea(_set[1])))

# print ('----------')

grafo.ubicar_espia_1(6, 5)
print('Espia 1 ubicado en (6,5)')
grafo.ubicar_espia_2(10, 3)
print('Espia 2 ubicado en (10,3)')
grafo.ubicar_aeropuerto(9, 100)
print('Aeropuerto ubicado en (9,100)')
print('-----------------------------')
print(grafo.obtener_ganador(True))
# print(grafo.obtener_ganador_euclideo())