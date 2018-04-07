## TP 1

Para este tp se usó python 3.5

### Parte 1: Cálculo empírico de tiempos de ejecución

Para la primera parte es necesario instalar jupyter y matplotlib:

```bash
pip install jupyter matplotlib
```


### Parte 2: Variante del algoritmo Gale-Shapley

Para la segunda parte, jupyter es opcional. Sirve para ejecutar el código interactivamente y ver la salida.

Para ejecutar el tp:

```bash
python tp1_2.py
```

Por defecto, va a generar las preferencias randomizadas basadas en una semilla, va a crear una carpeta `preferencias` y guardar los archivos ahí. Los parametros por defecto se pueden alterar desde el cógido. Por ejemplo, para cambiar la semilla, la carpeta, y no generar archivos sino leer los que ya están, hay que modificar el código de la función main de la siguiente forma:

```python
s = TPSolver(players=200, teams=20, seed=1000, path='mi_carpeta')
m = s.solve_tp(generate_files=False)
```