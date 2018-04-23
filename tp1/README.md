
# Instalación

Para este tp se usó python 3.5

## Parte 1: Cálculo empírico de tiempos de ejecución

Para la primera parte es necesario instalar jupyter y matplotlib:

```bash
pip install jupyter matplotlib
```

Luego se debe ejecutar el siguiente comando para poder comenzar con las pruebas

```bash
jupyter notebook
```

Se debe dirigiar hacia la carpeta tp1/tp1_1.ipynb y hay que ejecutar todas las
celdas del notebook desde el principio hasta el final

Seleccionar consecutivamente en cada celda

![](images/tp1-notebook.png)

Cuando aparece un [*] significa que se debe esperar a que termine la ejecución para poder
seguir ejecutando las otras celdas

![](images/tp1-notebook-loading.png)


## Parte 2: Variante del algoritmo Gale-Shapley

Para la segunda parte, jupyter es opcional. Sirve para ejecutar el código interactivamente y ver la salida.

Para ejecutar el tp:

```bash
python tp1_2.py
```

Por defecto, va a generar las preferencias randomizadas basadas en una semilla, va a crear una carpeta `preferencias` y guardar los archivos ahí. Los parametros por defecto se pueden alterar desde el cógido. Por ejemplo, para cambiar la semilla, la carpeta, y no generar archivos sino leer los que ya están, hay que modificar el código de la función main de la siguiente forma:

```python
s = TPSolver(players=200, teams=20, seed=1000, path='mi_carpeta')
m = s.solve_tp_fixed(generate_files=False)
```

Para ejecutar la versión anterior a la reentrega, hay que modificar el método, al que se llama a *solve_tp*: `s.solve_tp()`.
