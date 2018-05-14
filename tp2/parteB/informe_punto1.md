## Ejercicio 1

### Consigna

Dadas dos cadenas de texto S1 y S2 de longitud n, se desea determinar si la segunda es una rotación cíclica de la primera.

Ejemplo: DABRAABRACA es una rotación cíclica de ABRACADABRA

1. Resolverlo por fuerza bruta: Partiendo de S2 ir realizando rotación de 1 caracter y evaluando si son iguales. Determinar la complejidad del algoritmo.
2. Modificar la solución anterior del problema para que utilice el algoritmo de KMP (Knuth, Morris, Pratt) o Boyer-Moore. Explique por qué es una reducción y analice la complejidad resultante.
3. Evaluar si es posible mejorar la segunda solución llevándola a tener que realizar una única ejecución del algoritmo KMP (o Boyer-Moore). En caso afirmativo, vuelva a calcular la complejidad.

### Resolución

###### Explicación de los algoritmos
- *Algoritmo de fuerza bruta*:  ubicado en el script de python punto2-1-fuerzabruta.py, se realiza una comparación de cadenas común, recorriendo la cadena en toda su longitud y comparando cada elemento de una cadena con la otra.
- *Algoritmo ineficiente de KMP* : ubicado en el script de python kmp.py, es la funcion llamada kmp. El algoritmo primero crea una tabla en la función kmp_tabla a partir de una de las dos cadenas, con el objeto de almacenar el prefijo de la cadena más largo que sea a su vez un sufijo. Esta tabla es conocida también como función de fallo. Luego busca a partir de una cadena si hay una subocurrencia de la otra para poder determinar que existe ó no una rotación de strings.
- *Algoritmo eficiente de KMP* : al algoritmo anterior de KMP se lo lleva a una única ejecución para verificar si mejora su performance.

###### Punto 1
El algoritmo resuelto por fuerza bruta al entrar al primer loop, tiene una complejidad de $$O(n)$$ siendo n el tamaño de la cadena. Chequear luego la igualdad de una cadena con otra, en el peor de los casos es $$O(n)$$. Así que en total se llega como peor caso a $$O(n * m)$$

###### Punto 2
El algoritmo de KMP reduce comparaciones triviales y evita tener que recalcular matcheos como se hace con el algoritmo de Fuerza Bruta. 
Para mostrar que KMP es una reducción del problema anterior, si tenemos las cadenas X, Y y queremos saber si Y es una rotación cíclica de X, utilizamos el algoritmo de KMP(X+X, Y) de forma de buscar si el patrón Y aparece en la cadena X+X 
Si el algoritmo de KMP nos devuelve que sí, quiere decir que Y es una rotación ciclica de X. El motivo de esto radica en que X + X contiene todas las rotaciones ciclicas posibles de X, por lo que si Y es una rotación ciclica de X, el algoritmo KMP nos devolvera que el patrón Y está contenido en la cadena X+X.

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
Entrada
```
W = "HOLA"
S = "AHOL"
print(es_rotacion_eficiente(S,W))
```
Salida
```
True
```
Por último, este algoritmo realiza una comparación de 2 cadenas (X,Y) de longitud n para mostrar si son rotaciones entre si. La complejidad del mismo es $$O(n + n^2)~=O(n^2)$$

##### Punto 3
Sí, es posible y en este caso la complejidad va a ser de $$O(n)$$. 
Se hicieron las siguientes pruebas para mostrar que el resultado entre el algoritmo KMP no mejorado y el mejorado dieron ambos el mismo resultado:

```
W = "DABRAABRACA"
S = "ABRACADABRA"
print(es_rotacion_eficiente(S,W)) // El resultado dió True
print(es_rotacion_ineficiente(S,W)) // El resultado dió True


W = "DABRAABRACA1"
S = "ABRACADABRA3"
print(es_rotacion_eficiente(S,W)) // El resultado dió False
print(es_rotacion_ineficiente(S,W)) // El resultado dió False
```
