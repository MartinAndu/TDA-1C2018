\newpage

# Parte 2: Variante del algoritmo Gale-Shapley

## Consigna

Una liga amateur de Basketball tiene una manera extraña de iniciar la temporada. Un draft se realiza entre 200 jugadores anotados entre los 20 equipos que participaran. Tanto los jugadores como los equipos tienen una lista de preferencia donde establecen en orden decreciente sus elecciones. Cada listado es completo (tienen a todos los jugadores/equipos) y sin empates de preferencia. Se pretende construir un matching estable que termine con 20 equipos de 10 jugadores cada uno.

a) Construir el algoritmo de Gale-Shapley modificado para cumplir el requerimiento.

b) Probar que el mismo terminará en tiempo polinómico y siempre entregará un matching estable.

c) Ejecutar el algoritmo utilizando un set construido especialmente para el caso.

## Solución

Algoritmo de matching de Gale-Shapley devuelve un matching perfecto y estable entre dos conjuntos del mismo tamaño, y termina en tiempo polinómico ($O(n^2)$). El hecho de que sea perfecto nos asegura que no va a haber un elemento de cualquier conjunto sin matchear, y el hecho de que sea estable nos asegura de que en el matching resultante no haya ningún par, en el que un elemento prefiera una pareja de otro par, qué a su vez lo prefiere a él. El problema es que no es directamente aplicable, dado que la cantidad de jugadores y equipos no es la misma.

La solución que elegimos es extender los datos del problema para poder aplicarle el Gale-Shapley. Desde alto nivel, nuestra solución se puede explicar de la siguiente forma: en vez de 20 equipos, el segundo set se compone de 200 "vacantes", de modo que para cada equipo hay 10 vacantes. Las preferencias de las vacantes son las mismas que las del equipo al que corresponden. En las preferencias de los jugadores los equipos se reemplazan por las vacantes, de manera que si antes un jugador preferia equipo 1 antes que equipo 2, ahora va a pasar a preferir todas las vacantes del equipo 1 antes que cualquier vacante del equipo 2.

Nuestra resolución del trabajo práctico entonces consiste en:

1) Convertir el set de entrada, cambiando el set de equipos por set de vacantes y las preferencias de los jugadores.
2) Aplicar Gale-Shapley
3) Convertir el matching resultante a la forma inicial, es decir, reemplazar las vacantes por el equipo al que corresponden.

La complejidad de cada uno de esos pasos es (siendo n = cantidad de jugadores = cantidad de vacantes):

1) Consiste en recorrer las preferencias de cada jugador y cambiarles las preferencias de equipos por vacantes. Eso es $O(n^2)$. Luego a cada vacante se le agregan las preferencias del equipo correspondiente, lo cual tampoco debería tomar más de $n^2$ iteraciones.
2) Gale-Shapley termina en $O(n^2)$ (por la demostración del libro).
3) Consiste en recorrer el matching una vez: $O(n)$

La complejidad total del algoritmo de esta forma va a ser de $O(n^2)$, osea que el tiempo es polinomial.

*Observación*: en nuestra implementación el ranking se calcula buscando un elemento en una lista de preferencias, la búsqueda en una lista de Python es [O(n)](https://wiki.python.org/moin/TimeComplexity), por lo cual, nuestra implementación de Gale-Shapley en realidad va a tomar $n^3$ iteraciones en el peor caso. Ese tiempo sigue siendo polinomial, pero es bastante facil convertir el cálculo de ranking en O(1) usando una estructura de datos acorde.

Nos queda ver que el matching resultante es estable. Para eso queremos ver que no existan dos pares de jugador-equipo *$(a,e1)$* y *$(b,e2)$*, donde el jugador *a* prefiera el equipo *e2* y el equipo *e2* lo prefiera al jugador *a*. Para obtener ese resultado después de la ejecución de nuestro algoritmo, el Gale-Shapley debió haber devuelto un matching con *$(a,u)$* y *$(b,w)$*, donde *u* es una vacante de *e1* y *w* es una vacante de *e2*.

Supongamos que tal par existe. Eso significa en nuestra solución, que la última proposición de *a* fue hacía *u*. Si *a* no se le propuso a *w* previamente, entonces prefiere *u* por sobre *w* (osea que va a preferir cualquier vacante de *e1* antes de cualquiera de *e2*), lo cual contradice la suposición de que *a* prefiere el equipo *e2* por sobre *e1*. Si *a* se le propuso a *w*, entonces *w* rechazó su propuesta a favor de un jugador *c* (que puede ser el mismo que *b*, con el que terminó en el matching, u otro que prefiere por sobre *b*). Esto contradice la suposición de que *e2* prefiere *a* por sobre *b*. Por tanto, tales pares no pueden existir y el matching es estable.

---

Otra solución posible e incluso mejor (más eficiente) a este trabajo práctico es modificando el
algoritmo de Gale-Shapley para que se pueda matchear más de un elemento de un set al otro set (parecido a la solución del problema de hospitales y estudiantes). El orden de esa solución debería ser de *O(nm)*, donde n es la cantidad de jugadores y m es la cantidad de equipos.

\newpage
