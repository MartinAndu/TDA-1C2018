
## Ejercicio 2

### Consigna

Ustedes son los principales desarrolladores de un producto de software. El dueño multimillonario de la empresa para la que trabajan les pidió que visiten a clientes en n ciudades para discutir detalles técnicos. Él va a cubrirles todos los gastos, y deja que organicen ustedes mismos el itinerario. Como no pagan de sus bolsillos el costo de los aviones y no se llevan tan bien con el dueño, quieren conseguir la mayor cantidad posible de millas como viajeros frecuentes de la aerolínea.

Algunas reglas:

  - Todos los vuelos son directos.
  - Viajan siempre en grupo, todos juntos.
  - Los precios de los vuelos son fijos (no cambian según el día que vuelen).
  - Las millas que les da la aerolínea equivalen a la distancia (euclídea) entre las ciudades.
  - Van solo una vez a cada ciudad, y visitan ahí a todos los clientes de la misma.
  - Empiezan y terminan en la ciudad donde viven y trabajan.

Dar un algoritmo eficiente (pseudocódigo de alto nivel) para definir en qué orden van a visitar las n ciudades, o bien demostrar que el problema es difícil (NP-Completo o NP-Hard).

### Resolución

#### Suposiciones

Bajo la consigna del enunciado deducimos que conseguir la mayor cantidad de millas equivale a maximizar la distancia recorrida entre ciudades. Para completar la consigna, asumimos acertado agregar las siguientes suposiciones (después de consensuarlas con los ayudantes de la materia):

 - Todas las ciudades están conectadas.
 - De cualquier ciudad se puede ir a cualquier otra ciudad.

#### Análisis del problema

Podemos representar el problema como un grafo de la siguiente manera: las ciudades son nodos de ese grafo, y las aristas entre los nodos son las conexiones entre las ciudades correspondientes. Cada arista tiene como peso la distancia euclídea entre las ciudades correspondientes. Como todas las ciudades están conectadas, dicho grafo es completo, y como de cualquier ciudad se puede ir a cualquier otra, el grafo es no direccionado.

Dada dicha representación, el problema consiste en problema planteado es equivalente a encontrar un circuito que visita cada nodo exactamente una vez (circuito simple) y que maximiza el peso total del recorrido. Lo que buscamos es un circuito, y no un camino, por la necesidad de volver a la ciudad en la que arrancamos el recorrido.

Un problema ya conocido con una consigna muy parecida es el *problema del viajante* (TSP de sus siglas en inglés - Travelling Salesman Problem). El enunciado del problema de TSP es: dada una lista de ciudades, y las distancias entre ellas, encontrar el circuito (camino, que arranca y termina en la misma ciudad) de distancia mínima que visita todas las ciudades exactamente una vez. Es conocido que este problema es NP-Hard (su versión de decisión es NP-Complete, pero a nosotros nos interesa su versión de optimización). A continuación vamos a demostrar que nuestro problema es NP-Hard usando TSP.

#### Demostración de NP-Hardness

Un problema es NP-Hard si cualquier problema NP se puede reducir a ese problema en tiempo polinomial. Para demostrar que nuestro problema es NP-Hard, vamos a reducir el problema del viajante a él, y ver que esa reducción es lineal.

Supongamos que existe un algoritmo que resuelve nuestro problema. Ese algoritmo dado un grafo completo $G = (V, E)$ no direccionado con pesos, devuelve un circuito simple sobre ese grafo, en el que el peso total es máximo. Para obtener la solución del TSP sobre el mismo grafo $G$ (es decir, obtener el un circuito simple que minimiza el peso total) usando nuestro algoritmo, basta con asignarle peso $K - a_i$ a las aristas de $E$, donde $a_i$ es el peso inicial de la arista $e_i$, y $K$ es un número suficientemente grande, como para ser mayor que cualquiera de los pesos existentes (para que no queden pesos negativos).

Vamos a obtener el conjunto de aristas $E^{\prime}$, donde cada arista tiene el peso "invertido" respecto a $E$ (por ejemplo, la arista de mayor peso de $E^{\prime}$ es la arista de menor peso de $E$). Aplicando nuestro algoritmo a $G^{\prime} = (V, E^{\prime})$ vamos a obtener el circuito que maximiza el peso total sobre $G^{\prime}$. Resulta ser que ese mismo circuito es el que minimiza el peso total sobre $G$, por la forma de la que construimos $G^{\prime}$.

Como la conversión de aristas que realizamos para la reducción se puede hacer en tiempo lineal, ese paso no altera el orden total del algoritmo, por ende podemos afirmar que **nuestro problema es NP-Hard**.


#### Investigación adicional

Ya vimos que el problema es NP-Hard. Podríamos decir que nuestro problema es *NP-Completo*? Para eso, lo único que nos quedaría demostrar es que es NP, es decir, que dada una solución a nuestro problema existe un algoritmo que puede comprobar si es la solución óptima en tiempo polinomial.

Por la similitud al problema del viajante en su versión de optimización, para nuestro problema podemos afirmar que decir si un circuito es el que maximiza la distancia recorrida no es más *fácil* que encontrar el circuito óptimo. Por lo cual no podemos decir que es NP-Completo.

Durante la investigación sobre el problema nos encontramos con que existen algunos algoritmos polinomiales para encontrar el circuito con peso máximo, para la que es muy difícil encontrar un contraejemplo. En el campo de los problemas NP-Completos o NP-Hard esos algoritmos se conocen como heurísticas, y si bien no son precisos, suelen dar una solución óptima en bastantes casos. Para algunas heurísticas puede llegar a ser bastante complicado encontrar contraejemplos. En particular, en nuestro caso una dificultad adicional es que los pesos no son arbitrarios, sino son distancias euclídeas. Entonces cualquier conjunto de ciudades se podría representar en un plano euclídeo, y por ende a cualquier herística se le debería poder encontrar un contraejemplo gráficamente.

Un algoritmo muy simple para el que no pudimos encontrar un contraejemplo es el siguiente: del conjunto de las aristas ir seleccionando las de peso más grande, y agregándolas a la solución, siempre y cuando esa arista se pueda conectar (que la suma de las aristas incidentes en los nodos que conecta la arista en cuestión sea menor a 2).

