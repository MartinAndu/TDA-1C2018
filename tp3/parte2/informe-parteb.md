
## Ejercicio 2

### Consigna


### Resolución

#### Suposiciones

Bajo la consigna del enunciado deducimos que conseguir la mayor cantidad de millas equivale a maximizar la distancia recorrida entre ciudades. Para completar la consigna, asumimos acertado agregar las siguientes suposiciones (después de consensuarlas con los ayudantes de la materia):

 - Todas las ciudades están conectadas.
 - De cualquier ciudad se puede ir a cualquier otra ciudad.

#### Análisis del problema

Tenemos nodos, aristas y cada una de ellas tiene una capacidad máxima. La idea de la resolución radica en calcular el flujo máximo que pasará por la red dada como entrada según las especificaciones del ejercicio. Una vez que está calculado el flujo máximo, se toma la arista por la que pasa mayor cantidad de información. Se quita esa arista y se vuelve a calular el flujo máximo. Nuevamente se toma la arista cuyo flujo es máximo. En esas dos aristas es en donde se pondría el personal para vigilar la red.
El pseudocódigo del algoritmo es el siguiente:

#### Análisis de complejidad
Para este problema se utilizó una reducción utilizando un algoritmo ya conocido que es el de Ford-Fulkerson. La complejidad de este algoritmo es $O(Ef)$, donde $E$ es la cantidad de aristas y $f$ es el flujo máximo en el grafo. Esta justificación se da porque cada camino de aumento puede ser encontrada en un tiempo $O(E)$ e incrementa el flujo por una cantidad entera de a lo sumo $1$ con una cota máxima de $f$.
Existe una variación de Ford-Fulkerson que garantiza terminación y un tiempo de ejecución independientemente del valor del máximo flujo. Este algoritmo se llama Algoritmo de Edmonds-Karp. La complejidad de dicho algoritmo es $O(VE^2)$ donde $V$ es la cantidad de vértices y $E$ la cantidad de aristas. En este trabajo se utilizó esta variante.

