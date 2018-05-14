
## Ejercicio 3

### Consigna

Una universidad quiere dictar un conjunto de cursos C1, C2 … Cn donde cada curso se puede dar solo en el intervalo de tiempo Ti, ya que los docentes tienen poca flexibilidad horaria. Puede que varios cursos se den a la vez, por ejemplo el curso 1 puede dictarse de 3 a 6 y el curso 2 de 4 a 8. Conocemos el horario de inicio y finalización de cada uno de los cursos. El objetivo es ver cuál es la menor cantidad de aulas necesarias para acomodar todos los cursos (suponer que todas las aulas son iguales).

  1) Dar un algoritmo eficiente (pseudocódigo de alto nivel) que resuelva el problema.
  2) Reducir el problema a una instancia de coloreo de grafos, en su versión de optimización (minimizar la cantidad de colores).
  3) A partir de los dos puntos anteriores, ¿podemos asegurar que P = NP? ¿Por qué?


### Algoritmo eficiente

Se está buscando un algoritmo que, dado como entrada un set de intervalos correspondientes al tiempo en el que se pueden dar los cursos, definir cual es la cantidad mínima de aulas, necesarias para dar todos los cursos. Cada intervalo *i* es un par *(s(i), f(i))*, donde *s(i)* es el tiempo de comienzo del intervalo, y *f(i)* es el tiempo de finalización de ese intervalo. Un intervalo *j* se superpone con un intervalo *i* si existe algún punto *t(j)* del intervalo *j* tal que *s(i) <= t(j) <= f(i)*.

Los cursos superpuestos se tienen que dar en aulas diferentes. La cantidad de aulas buscada va a ser igual a la cantidad máxima de cursos superpuestos en algún momento en la línea de tiempo, por ende un algoritmo que detecte la máxima cantidad de superposiciones nos dará como resultado la cantidad mínima de aulas que se van a necesitar.

Una solución polinomial sería una variante simplificada del algoritmo para problema de coloreo de intervalos. La idea es recorrer los intervalos, ordenandos por su tiempo de comienzo, y ver con cuantos intervalos previos se superpone el intervalo actual. El pseudocódigo de esa solución es el siguiente:


```
def minima_cantidad_recursos(intervalos)
    intervalos_ordenados := ordenar intervalos por tiempo de comienzo

    resultado := 0
    para cada intervalo j en intervalos_ordenados:
        cantidad_de_recursos := 0
        para cada intervalo i en intervalos_ordenados que le precede a j:
            si (i se superpone con j):
                cantidad_de_recursos := cantidad_de_recursos + 1

        resultado := max(resultado, cantidad_de_recursos)

    return resultado
```

El ordenamiento de los intervalos se resuelve en $O(nlog(n)$, pero se puede ver por los dos loops internos que el orden total del algoritmo termina siendo $O(n^2)$. De hecho, el orden termina siendo el mismo que el de un algoritmo por fuerza bruta, en el cada intervalo se compara con todos los demás. Podemos plantear un algoritmo más eficiente, si también consideramos los tiempos de finalización.

La idea detrás del algoritmo mejorado es la siguiente: si los intervalos se ordenan por tiempos de comienzo por un lado, y por tiempos de finalización por el otro, la profundidad de los intervalos anteriores al tiempo de finalización $f_i$ es igual a la cantidad de intervalos que empezaron antes de $f_i$ menos la cantidad de intervalos que terminaron antes de $f_i$, que es igual al $i - 1$ (por el orden de los tiempos de finalización). El pseudocódigo de ese algoritmo es el siguiente:


```
def minima_cantidad_recursos_mejorado(intervalos)
    n := tamaño (intervalos)
    intervalos_comienzo := ordenar intervalos por tiempo de comienzo
    intervalos_fin := ordenar intervalos por tiempo de finalización

    resultado := 0
    profundidad_actual := 0
    i := 0; j := 0

    mientras (i < n y j < n):
        si (intervalos_comienzo[i] < intervalos_fin[j]):
            profundidad_actual := profundidad_actual + 1
            resultado := max(resultado, profundidad_actual)
            i := i + 1
        sino:
            profundidad_actual := profundidad_actual - 1
            j := j + 1

    return resultado
```


La ejecución de esta mejora del algoritmo incluye dos ordenamientos, que se hacen en $O(2*nlog(n))$, y el procesamiento que toma como máximo $O(2n)$. El orden final es $O(2*nlog(n) + 2n) = O(nlog(n))$.


### Reducción a coloreo de grafos

Un coloreo $X(G)$ es una función que dado un vértice (coloreo de vértices) o una arista (coloreo de aristas) devuelve una etiqueta, tradicionalmente llamada "color". El **Problema de Coloreo de Grafos (GCP)** en su versión de optimización tiene el siguiente enunciado: dado un grafo $G$, retornar un coloreo $X(G)$ tal que no haya dos elementos adyacentes del grafo $G$ con el mismo color, que utilice la mínima cantidad de colores. GCP en su versión de optimización es conocido *NP-Hard*, por ende no se conoce un algoritmo eficiente que lo solucione.

Suponiendo que existe un algoritmo que soluciona GCP, para reducir nuestro problema (que vamos a llamar mínima cantidad de recursos) al GCP, tendremos que convertir la entrada de nuestro problema a la entrada del GCP, y la salida del GCP a la salida del nuestro problema. El orden de ambas conversiones no tiene que ser mayor al orden del algoritmo que soluciona GCP para que la reducción tenga sentido. Sin embargo, como no se conoce ningún algoritmo eficiente para solucionar GCP, nos alcanza con que las conversiones sean polinomiales.

```
Sea Y la entrada y K la salida de nuestro problema,
Buscamos una reducción tal que:

C1(Y) -> X
GCP(X) -> R
C2(R) -> K

Donde las funciones de conversión C1 y C2 son polinomiales.
```

Una forma fácil de hacer la conversión de la entrada $C1$ es creando un grafo $G = (V, E)$, donde los vértices son los intervalos. Un par de vértices es conectado por una arista si y solo si los intervalos correspondientes a esos vértices se superponen. Si usamos esa representación como entrada al algoritmo que soluciona GCP (en su versión de coloreo de vértices), vamos a obtener como resultado un coloreo $X(G)$ tal que si dos vértices están conectados por una arista (es decir dos intervalos se superponen), tienen color diferente. Como el algoritmo GCP optimiza la cantidad de colores usados, para realizar la conversión de la salida $C2$ nos basta con contar la cantidad de colores diferentes en el coloreo $X(G)$.

La primera conversión $C1$ se puede hacer por fuerza en $O(n^2)$ (buscando para cada intervalo todos los intervalos con los que se superpone). Posiblemente no sea la conversión más eficiente, pero no nos va a alterar el orden de la reducción final. La segunda conversión se hace en tiempo lineal, recorriendo los vértices de $G$ y consultando su color en $X(G)$.

### ¿P = NP?

Redujimos un algoritmo, que sabemos del primer punto que tiene una solución en $O(nlog(n))$ a un problema NP-Hard del cual no se conoce una solución eficiente. La solución final quedó del orden del problema al que redujimos, pero la reducción es válida, porque de esta manera demostramos que nuestro algoritmo no es más difícil que el algoritmo que soluciona GCP.

Sin embargo no podemos hacer la reducción inversa, es decir conseguir una conversión de entrada de GCP a la entrada a nuestro algoritmo, y otra conversión de la salida de nuestro algoritmo, de modo que las conversiones no tengan mayor orden que $O(nlog(n))$. Por ende, no podemos afirmar que $P = NP$.

\newpage
