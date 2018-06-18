
\newpage

# Instalación y ejecución

El juego se desarrolló y se probó con Python 3.5

## Parte 1

Desde la carpeta `parte1` se ejecuta de la siguiente manera:

```bash
python TP3-1.py <tablero> <lanzaderas> <estrategia>
```

Donde:

 - `<tablero>` es ruta al archivo del tablero
 - `<lanzaderas>` es un el número de lanzaderas. Tiene que ser un número entero.
 - `<estrategia>` es el nombre de la estrategia a usar. Puede ser `naive`, `greedy` o `dinamico`.

Ejemplo de ejecución:

```bash
python TP3-1.py tablero3 3 dinamico
```

## Parte 2

Desde la carpeta `parte2` se ejecuta de la siguiente manera, pasando una ruta a un archivo de red secreta:

```bash
python TP3-2.py <archivo de red secreta>
```

Por ejemplo:

```bash
python TP3-2.py redsecreta2.map
```
