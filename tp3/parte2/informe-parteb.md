
## Ejercicio 2

### Consigna

#### Análisis del problema

Tenemos nodos, aristas y cada una de ellas tiene una capacidad máxima. La idea de la resolución radica en calcular el flujo máximo que pasará por la red dada como entrada según las especificaciones del ejercicio. Una vez que está calculado el flujo máximo, se toma la arista por la que pasa mayor cantidad de información. Se quita esa arista y se vuelve a calular el flujo máximo. Nuevamente se toma la arista cuyo flujo es máximo. En esas dos aristas es en donde se pondría el personal para vigilar la red.
El pseudocódigo del algoritmo es el siguiente:
Para el pseudocódigo definimos:
$C(u,v)$ como capacidad de la arista que une los vértices $u$ y $v$ en el grafo original.
$G_f(u,v)$ como capacidad de la arista que une los vértices $u$ y $v$ en el grafo residual.
$flujo_maximo_arista(u,v)$ tiene cuanto flujo pasa por esa arista
```
para cada arista (u,v) \in G:
    G_f(u,v) = 0
    G_f(v,u) = 0

mientras \exists un camino $p$ desde la fuente al sumidero en el grafo residual:
    c_f := $min\{G_f(u,v) : (u, v) \in $p$\}$
    para cada arista (u,v) en p:
        G_f(u, v) -= c_f
        G_f(v, u) += c_f
        flujo_maximo_arista(v,u) = G_f(v,u)

ordenar de menor a mayor los valores de flujo_maximo_arista \forall (u,v) 
tomar el ultimo
```

#### Análisis de complejidad
Para este problema se utilizó una reducción utilizando un algoritmo ya conocido que es el de Ford-Fulkerson. La complejidad de este algoritmo es $O(Ef)$, donde $E$ es la cantidad de aristas y $f$ es el flujo máximo en el grafo. Esta justificación se da porque cada camino de aumento puede ser encontrada en un tiempo $O(E)$ e incrementa el flujo por una cantidad entera de a lo sumo $1$ con una cota máxima de $f$. Los caminos de aumento busca caminos de fuente a sumidero que sean acíclicos
Existe una variación de Ford-Fulkerson que garantiza terminación y un tiempo de ejecución independientemente del valor del máximo flujo. Este algoritmo se llama Algoritmo de Edmonds-Karp. La complejidad de dicho algoritmo es $O(VE^2)$ donde $V$ es la cantidad de vértices y $E$ la cantidad de aristas. En este trabajo se utilizó esta variante.

#### Múltiples fuentes y múltiples sumideros
Podemos transformar el problema de múltiples fuentes y sumideros a un problema conocido de una fuente y un sumidero. Para cada una de las fuentes originales podemos conectarla con una arista de capacidad infinita (o en terminos programáticos un número muy grande) a una nueva fuente. De manera análoga hacer lo mismo con los sumideros. De esta manera podemos implementar lo que ya estudiado y analizado para un caso mucho más real.