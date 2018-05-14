\newpage

# Parte 2

## Ejercicio 1

### Consigna

Dadas dos cadenas de texto S1 y S2 de longitud n, se desea determinar si la segunda es una rotación cíclica de la primera.

Ejemplo: DABRAABRACA es una rotación cíclica de ABRACADABRA

1. Resolverlo por fuerza bruta: Partiendo de S2 ir realizando rotación de 1 caracter y evaluando si son iguales. Determinar la complejidad del algoritmo.
2. Modificar la solución anterior del problema para que utilice el algoritmo de KMP (Knuth, Morris, Pratt) o Boyer-Moore. Explique por qué es una reducción y analice la complejidad resultante.
3. Evaluar si es posible mejorar la segunda solución llevándola a tener que realizar una única ejecución del algoritmo KMP (o Boyer-Moore). En caso afirmativo, vuelva a calcular la complejidad.

### Resolución

#### Algoritmo de fuerza bruta

El algoritmo de fuerza bruta consiste en ir rotando el string (removiendo el primer caracter y poniendolo al final), y comparando con el segundo string. Si después de realizar `n` (donde `n` es es el tamaño de la primera string) comparaciones, ninguna comparación dió verdadero - las cadenas no son rotaciones cíclicas. La comparación se realiza recorriendo la cadena en toda su longitud y comparando cada elemento de una cadena con la otra.

Cabe aclarar que para que dos cadenas sean rotaciones cíclicas, necesariamente tienen que tener la misma cantidad de caracteres, entonces tanto esta implementación como la siguiente verifica esta condición y no hace procesamiento extra si da falso.

El algoritmo resuelto por fuerza bruta al entrar al primer loop, tiene una complejidad de $O(n)$ siendo n el tamaño de la cadena. Chequear luego la igualdad de una cadena con otra, en el peor de los casos es $O(n)$. Así que en total se llega como peor caso a $O(n^2)$

El código de esta solución se puede ver en el archivo `fuerzabruta.py`.

#### Algoritmo ineficiente con KMP

El algoritmo Knuth–Morris–Pratt (KMP) se utiliza para encontrar subocurrencias de una cadena de texto en otra. La implementación de ese algoritmo utilizada por nosotros, dadas dos cadenas de caracteres devuelve el índice de ocurrencia de la segunda string en la primera, o 0 en el caso de que no exista. Internamente utiliza una tabla generada a partir de la primer cadena, conocida también como función de fallo, con el objeto de almacenar el prefijo de la cadena más largo que sea a su vez un sufijo. El cálculo de la tabla se realiza en $O(n)$ y la posterior búsqueda de subocurrencias toma $O(n)$. El orden total de esta implementación es de $O(2n) = O(n)$.

El uso más directo del algoritmo KMP para solucionar nuestro problema es reemplazar la comparación de string en implementación de fuerza bruta por la llamada al algoritmo KMP. Si dos strings son iguales, necesariamente cualquiera de las dos es una subocurrencia de la otra. Entonces en este caso estamos haciendo una reducción de comparación de strings al algoritmo de KMP. Para poder utilizar esta reducción, primero debemos verificar que las cadenas tengas el mismo tamaño.

La conversión de la entrada no es necesaria, ya que la comparación de dos cadenas tiene las mismas dos cadenas que el algoritmo de KMP en nuestra implementación. La salida del algoritmo de KMP nos dice a partir de qué índice una cadena es subocurrencia de la otra, o un índice menor al primero si no hubo subocurrencia. Podemos convertir esta salida en una decisión sobre si las cadenas son iguales en $O(1)$. De esta manera la reducción no altera el orden del algoritmo que reducimos.

El orden de este algoritmo sigue siendo de $O(n^2)$, ya que reemplazamos la comparación de strings por una llamada a KMP, que tiene orden $O(n)$.

El código tanto de esta implementación, como el de la siguiente se puede ver en el archivo `kmp.py`.

Si el código de `kmp.py` se modifica de la siguiente forma:

```
W = "HOLA"
S = "AHOL"
print(es_rotacion_ineficiente(S,W))
```

La salida de la ejecución de `python kmp.py` es la siguiente:

```
True
```

#### Mejora al algoritmo con KMP

Una forma de resolver el problema de deducir si dos strings (X e Y) son rotación cíclica entre si, es buscando si Y es una subocurrencia de una concatenación de X con X. El motivo de esto radica en que X + X contiene todas las rotaciones ciclicas posibles de X, por lo que si Y es una rotación ciclica de X, el algoritmo KMP nos devolvera que el patrón Y está contenido en la cadena X+X.

El orden de este algoritmo es de $O(2n) = O(n)$.

Como ejemplo:

Datos

```
X = HOLA
Rotaciones de HOLA:
HOLA
OLAH
LAHO
AHOL

X + X = HOLAHOLA
Y = OLAH
```

Si el código de `kmp.py` se modifica de la siguiente forma:

```
W = "HOLA"
S = "AHOL"
print(es_rotacion_eficiente(S,W))
```

La salida de la ejecución de `python kmp.py` es la siguiente:

```
True
```
