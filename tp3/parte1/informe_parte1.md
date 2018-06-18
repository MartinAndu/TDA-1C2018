
# Parte 1: Juego de batalla naval

## Consigna

Podemos modelizar el juego como:

 - El juego se realizar por turnos.
 - El bando “A” tiene X barcos. Cada uno de ellos tiene Vi puntos de vida.
 - El bando “B” tiene Y lanzaderas de misiles. Cada una tiene un alcance global (es decir que llega a cualquier lugar que desee.
 - El tablero de juego tiene forma de grilla. Con igual cantidad de filas que barcos iniciales. Las columnas son ilimitadas (tantas como se necesiten en el juego). A efectos programáticos se puede considerar que al llegar al final de la grilla se “teletransporta” al inicio de la misma
 - Cada barco se ubica al inicio de una fila y se desplaza por turno en 1 posición (a la columna siguiente).
 - Cada lanzadera de misiles puede disparar 1 misil por turno
 - El daño que puede realizar un misil está únicamente ligado a la grilla en la que se encuentra el barco en ese momento.
 - Los valores de daño están predefinidos en la grilla al inicio del juego, no se modifican y son conocidos por “A”
 - Por cada turno que pasa el equipo “B” recibe un punto por cada barco que siga en el juego
 - Los barcos permanecen en el juego y avanzan siempre que conserven puntos de vida.
 - Los puntos de vida y la cantidad de daño son valores enteros positivos.
 - El objetivo de “B” es minimizar la cantidad de puntos logrados por “A”

Tenemos 2 amigos que usaran el juego. “Greedo” y “Dinámico”. Jugarán partidas entre ellos alternando entre el bando “A” y “B”. Siempre el juego se realizará de a pares conservando la misma disposición de tablero y fichas (lanzaderas y barcos).

 - Diseñar para “Greedo” una estrategia greedy y para “Dinamico” una estrategia mediante programación dinámica. Presentar el pseudocódigo. Analizar sus complejidades
 - Programar el juego permitiendo tomar diferentes grillas, lanzaderas y barcos. debe poder usarse cualquiera de las dos estrategias realizadas en el punto 1.
 - Determinar si la solución greedy es óptima o si no lo es bajo qué condiciones puede serlo.
 - (opcional) Realice una interfaz gráfica para visualizar la evolución del juego
 - Imagine que el jugador “A” tiene la posibilidad de seleccionar para cada barco la columna inicial donde se ubicará su barco. Diseñe un algoritmo que le permita aumentar la cantidad a lograr. Analice su complejidad

Grilla:

Se deberá contar con un archivo con la definición del tablero de juego. El mismo deberá tener el siguiente formato:

 - Un renglón por fila de grilla
 - El primero número de cada fila es la vida del barco que se movera en ella.
 - Seguido de números enteros separados por espacio para cada daño de recibir un misil en la columna

Ejemplo:

```
800 20 40 10 120
300 80 30 90 0
```

El número de filas determinará la cantidad de barcos del jugador “A”. Por parámetro del programa se le debe pasar la grilla a utilizar, la estrategia y la cantidad de lanzaderas disponibles.

La salida del programa debe mostrar por cada turno:

 - Número de turno
 - Cantidad de barcos disponibles
 - Vida restante de cada barco y daño potencial según celda en la que se encuentra
 - Objetivos seleccionados por las lanzaderas.
 - Puntos acumulados

A la finalización debe indicar

 - Turnos totales
 - Puntos acumulados.


## Resolución del ejercicio

### Supuestos

Se tomaron los siguientes supuestos:

 - En un turno, primero disparan los lanzaderos, luego se mueven los barcos.
 - Solo hay que desarrollar una estrategia para los disparos de los lanzaderos. Los barcos siempre avanzan un paso cada turno.

### Planteo del juego

La resolución de nuestro juego se puede encontrar en el archivo `batalla_naval.py` que define la lógica del juego (definida en la clase `Juego` )y las clases y estructuras de datos que se van a utilizar. El juego necesita recebir como parametros la ruta del archivo con información sobre el tablero, la cantidad de lanzaderos a utilizar y una instancia de `Estrategia`. `Estrategia` es una clase de la que se espera que esté definido el método `siguiente_turno`, que dado el tablero, cantidad de lanzaderos, información sobre barcos y número de turno actual devuelva una lista de barcos, a los que el juego deberá disparar en ese turno.

La lógica principal del juego es la siguiente:

1) Se parsea el archivo con el tablero específicado, los valores se guardan en estructuras internas que se van a explicar más adelante.
2) Se entra al loop principal, en el que:
2.1) Se le pide a la estrategia a qué barcos disparar en el turno actual
2.2) Se aplica a los barcos el daño de los misiles disparados
2.3) Se verifica cuantos barcos quedaron vivos. Si ninguno, se sale del loop principal y el juego termina. En el otro caso, se suma la cantidad de barcos vivos a los puntos acumulados.
2.4) Finalmente los barcos se mueven una posición para adelante, y se vuelve al comienzo del loop

### Estructuras de datos

A continuación se explicarán las estructuras de datos utilizadas. Estas estructuras van a ser usadas por el juego, tanto para mantener la información sobre el estado del juego, como para proveerselas a la estrategia. La estrategia a su vez tendrá que usarlas para calcular los barcos a impactar en un turno.

Supongamos que el contenido del archivo de tablero es el del ejemplo del enunciado:

```
800 20 40 10 120
300 80 30 90 0
```

El juego va a guardar el tablero en un diccionario `tablero`, en el que las claves son los números de los barcos (que siempre se van a enumerar de 0 a *n-1*, donde *n* es la cantidad de filas en el archivo), y los valores son listas con daño potencial de cada posición. De esta forma, por ejemplo, para el barco 0 en la posición 0 el daño potencial es de 20. Esta estructura se mantiene estática en el transcurso del juego.

```python
{
  0: [20, 40, 10, 120],
  1: [80, 30, 90, 0]
}
```

La información de los barcos se va a guardar en un diccionario `barcos`, que como claves tendrá los números de los barcos, y como valores, diccionarios con la información de cada barco. Ese diccionario de información tendrá la posición actual de cada barco, y su vida actual.

```python
{
  0: {'posicion': 0, 'vida': 200},
  1: {'posicion': 0, 'vida': 300}
}
```

Para dar un ejemplo, supongamos que tenemos 2 lanzaderos. En el primer turno, el primer lanzadero le dispara al barco 0, y el segundo al barco 1. Al principio del turno 2, el diccionario de barcos tendrá el siguiente contenido:

```python
{
  0: {'posicion': 1, 'vida': 180},
  1: {'posicion': 1, 'vida': 220}
}
```


## Estrategia Greedy

### Algoritmo elegido



## Estrategia Dinámica

### Resolución teórica

Para la estrategia dinámica se plantearon varios algoritmos. El que mejores resultados dió tiene la siguiente idea como base: dada la posición actual de los barcos, el mejor conjunto de disparos es el que minimiza la cantidad de puntos logrados en la posición actual y el de los disparos consecutivos (alterando la posición por los disparos elegidos).

Esta idea se puede plantear de la siguiente forma: supongamos que $n$ es nuestra posición actual, $d$ es un conjunto de disparos (con tantos elementos, cuantos lanzaderos tengamos), y $f(n, d)$ es una función que dada la posición $n$ y disparos $d$ cuantos puntos va a obtener el jugador del equipo contrario. Supongamos que $D$ son todos los diparos que podemos hacer y $n+1$ es la posición en la que vamos a quedar si impactamos disparos $d_i$. Podemos plantear la siguiente recurrencia:

$$
OPT(n, d) = f(n, d) + min(OPT(n+1, d_i) \forall d_i en D)
$$

Necesitamos agregar una condición de corte: si un set de disparos resulta en que el contrincante no gane puntos, es el set de disparos óptimo, es decir, si $f(n, d) = 0$ entonces $OPT(n, d) = 0$.

La llamada inicial (la del primer turno) de esta forma sería:

$$
primer_turno(n) = min(OPT(n, d_i) \forall d_i en D)
$$


### Resolución práctica

