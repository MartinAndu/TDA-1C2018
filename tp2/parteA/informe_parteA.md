\newpage

# Parte 1: Spy Vs Spy

## Consigna

Dos Agentes secretos intentan hacerse con unos informes clasificados. El espía 1 - que es el que los tiene - se encuentra en un punto de la ciudad escondido y tiene que ir al aeropuerto. El espía 2 se encuentra en otro punto de la ciudad y desea interceptarlo. Para eso tiene que llegar al aeropuerto antes que su rival y emboscarlo.

Dado un mapa de una ciudad, las ubicaciones de los espías y el aeropuerto determine quién se quedará con los informes.
Repita el procedimiento pero introduciendo costos en los caminos.
Analice la complejidad añadida si se solicita retornar el camino realizado por cada espía en los pasos 1 y 2.
Realiza los pasos 1 y 2 nuevamente retornando como salida de ejecución los caminos realizados por cada espía.
El mapa de la ciudad:

El mapa de la ciudad y sus caminos esta representados por un grafo que se almacena en un archivo con formato texto.
Cada vértice del grafo está representado por 2 coordenadas: x e y. Estas coordenadas solo toman valores numéricos enteros y positivos.
Las conexiones entre los puntos del grafo se almacenan una por línea del archivo “mapa.coords” de la forma:

p1.x p1.y - p2.x p2.y

Ejemplo:

```
10 3 - 6 5
4 134 - 9 100
```

Para el punto 1 considere simplemente la cantidad de puntos del mapa recorridos como la distancia
Para el punto 2, el costo de cada camino está dado por la distancia euclídea de cada tramo.
Adicionalmente el programa recibirá por línea de comandos las posiciones del espía 1, 2 y el aeropuerto que deberán ser alguno de los puntos del mapa (se ingresaran cada uno como un numero entero positivo equivalente a la posición en el archivo del mapa de un punto del grafo).

Los programas deben funcionar para cualquier mapa de ciudad. Los algoritmos deben ser eficientes y adecuados al tipo de problema.

## Algoritmo de resolución

### Uso de Algoritmo
Cuando se trabaja con distancias unitarias, es decir, la distancia es la cantidad de nodos entre uno dado y otro, se aplica el algoritmo BFS.
Cuando se trata de distancias euclideas, se aplica un algoritmo de Dijkstra con cola de prioridad. Este algoritmo consiste en aplicar un Dijkstra para encontrar el camino mínimo entre varios vértices pero con la variante de agregar una cola de prioridad.

### Explicacion

En la cola de prioridad se hace un push como primer elemento de una tupla de (nodo, distancia). Se extrae de esta estructura esta tupla . A patir de eso, se busca el nodo más cercano y se hace un push en la cola de prioridad de la tupla (nodo, distancia). Se recorre así el grafo conexo, guardando en la cola las distancias mínimas que fue encontrando. Se realiza este procedimiento hasta que la cola esté vacía.

### Justificación del algoritmo
Cuando se trabaja con las distancias unitarias, el algoritmo BFS es más eficiente que aplicar Dijkstra. En cada iteración expande la búsqueda por una arista. Esto tiene el efecto de encontrar el menor número de pasos que toma hasta un nodo dado desde la raíz. En cambio, Dijkstra devuelve el camino mínimo desde el origen hasta cada nodo, pero se puede trabajar con distintas distancias.

En un Dijkstra común para este problema se encontraría la solución esperada pero es ineficiente porque en el peor de los casos que los espías estén bastante alejados entre sí y entre el aeropuerto, es de $O(|E| + |V|^2)$

Al agregarse una estructura nueva que en nuestro caso es la cola de prioridad, se permite guardar el grafo con las mínimas distancias y se llega a una complejidad de $O( E \log v)$ en el peor caso.

En ambos casos se guarda un diccionario con clave un objeto tipo Nodo y un valor otro objeto del mismo tipo. Este diccionario está pensado para ir guardando desde dónde se llegó a cada nodo. Finalmente, para mostrar la información en pantalla, se toma el nodo correspondiente al espía 1, se obtiene el nodo padre, se vuelve a repetir esta operación hasta que el nodo padre sea igual a nulo. Análogamente, se hace lo mismo con el nodo correspondiente al espía 2.
Llenar este diccionario en ambos algoritmos no añade complejidad. Dado que, tanto agregar como consultar un diccionario en Python es $O(1)$.
Para mostrar el camino existe el método `reconstruir_camino(self, diccionario, inicial)` que se llama desde `obtener_ganador`. La complejidad de dicho método es $O(N)$
En Python tanto consultar como agregar el caso promedio es $O(1)$. Existen casos muy particulares, donde la complejidad es $O(N)$. Esto sucede cuando hay
colisiones. En ese caso, se puede sobreescribir el método `__hash__` para evitar que esto suceda y de esta manera no aumentar la complejidad.

### Resolución

El código del algoritmo se puede encontrar en los archivos `Grafo.py` y `Nodo.py`, y se puede ejecutar el problema, modificando el archivo `mapa.coords` y llamando al script `TP2-1.py` de la siguiente forma:

```python
python TP2-1.py
```

Si el contenido de `mapa.coords` es el siguiente:

```
10 3 - 6 5
6 5 - 5 4
5 4 - 4 134
10 3 - 4 134
4 134 - 5 34
5 34 - 9 100
```

La salida de esa ejecución es la siguiente:

```
Espia 1 ubicado en (6,5)
Espia 2 ubicado en (10,3)
Aeropuerto ubicado en (9,100)
-----------------------------
El ganador es el espia 2 y la ruta que recorrio fue (10,3) (4,134) (5,34) (9,100)
```
