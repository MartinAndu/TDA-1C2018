
\newpage

# Parte 2: Sabotaje!

## Consigna

Son agentes secretos de la organización C.O.N.T.R.O.L y reciben una información anónima que los pone en alerta: La organización K.A.O.S planea sabotear la red secreta de transporte de información. Hace unos días se reportó el robo de una copia del mapa maestro de la red. Dan por supuesto que el robo fue de sus rivales y que ellos conocen las debilidades de su red. Siendo que únicamente tienen personal suficiente para vigilar 2 ejes de su red, que únicamente se pueden sabotear ejes (y no vertices) y que los saboteadores quieren hacer el máximo daño posible:

 - Diseñe un algoritmo genérico que funcione con cualquier tipo de red que determine qué ejes vigilar. Preséntelo con un pseudocódigo, explique su funcionamiento y si el mismo además es óptimo.
 - Analice la complejidad del mismo. De igual manera analice si utiliza alguna reducción.
 - Programe el algoritmo.
 - Si es necesario programe el algoritmo para determinar el flujo máximo. Utilícelo para calcular el de la red antes y después de los posibles sabotajes.
 - En una situación real existirán varias fuentes y varios sumideros. Explique y analice una forma de resolver el mismo problema en este caso.

Red Secreta:

El mapa de la red se debe obtener de un archivo llamado “redsecreta.map” con el siguiente formato:

 - Cada línea del archivo corresponde a un eje de la red que une 2 vértices y su capacidad
 - Los ejes están etiquetadas por números enteros
 - La capacidad son números enteros.
 - La fuente estará etiquetada como el número 0 (cero)
 - El sumidero estará etiquetado como el número 1 (uno)


## Análisis del problema

Tenemos nodos, aristas y cada una de ellas tiene una capacidad máxima. La idea de la resolución radica en calcular el flujo máximo que pasará por la red dada como entrada según las especificaciones del ejercicio. Una vez que está calculado el flujo máximo, se toma la arista por la que pasa mayor cantidad de información. Se quita esa arista y se vuelve a calular el flujo máximo. Nuevamente se toma la arista cuyo flujo es máximo. En esas dos aristas es en donde se pondría el personal para vigilar la red.
El pseudocódigo del algoritmo es el siguiente:
Para el pseudocódigo definimos:
$C(u,v)$ como capacidad de la arista que une los vértices $u$ y $v$ en el grafo original.
$G_f(u,v)$ como capacidad de la arista que une los vértices $u$ y $v$ en el grafo residual.
$flujo_maximo_arista(u,v)$ tiene cuanto flujo pasa por esa arista

```
para cada arista (u,v) de G:
    G_f(u,v) = 0
    G_f(v,u) = 0

mientras exista un camino p desde la fuente al sumidero en el grafo residual:
    c_f := se toma minimo {G_f(u,v) : (u, v) en camino p}
    para cada arista (u,v) de p:
        G_f(u, v) -= c_f
        G_f(v, u) += c_f
        flujo_maximo_arista(v,u) = G_f(v,u)

ordenar de menor a mayor los valores de flujo_maximo_arista para todo (u,v)
tomar el ultimo
```

## Análisis de complejidad
Para este problema se utilizó una reducción utilizando un algoritmo ya conocido que es el de Ford-Fulkerson. La complejidad de este algoritmo es $O(Ef)$, donde $E$ es la cantidad de aristas y $f$ es el flujo máximo en el grafo. Esta justificación se da porque cada camino de aumento puede ser encontrada en un tiempo $O(E)$ e incrementa el flujo por una cantidad entera de a lo sumo $1$ con una cota máxima de $f$.
Los caminos de aumento busca caminos de fuente a sumidero que sean acíclicos. La complejidad del algoritmo de caminos de aumento puede ser muy mala si se eligen mal los caminos, puede ser del orden de la capacidad máxima, la cual puede ser exponencial en el tamaño de la entrada.
Existe una variación de Ford-Fulkerson que garantiza terminación y un tiempo de ejecución independientemente del valor del máximo flujo. Este algoritmo se llama Algoritmo de Edmonds-Karp. La complejidad de dicho algoritmo es $O(VE^2)$ donde $V$ es la cantidad de vértices y $E$ la cantidad de aristas. En este trabajo se utilizó esta variante.

## Múltiples fuentes y múltiples sumideros
Podemos transformar el problema de múltiples fuentes y sumideros a un problema conocido de una fuente y un sumidero. Para cada una de las fuentes originales podemos conectarla con una arista de capacidad infinita (o en terminos programáticos un número muy grande) a una nueva fuente. De manera análoga hacer lo mismo con los sumideros. De esta manera podemos implementar lo que ya estudiado y analizado para un caso mucho más real.
