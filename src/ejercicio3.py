################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from ejercicio2 import es_minimo, es_maximo
"""
### 3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre
dos listas.Siendo 0 sin superposición y uno para cada elemento
superpuesto.
```python
['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
```
y
```python
['H', 'o', 'l', 'a']
```
Tienen una superposición de cuatro elementos.
#### Extra #1
Indicar en lugar de la cantidad de caracteres superpuestos, la posicion
de inicio de la superposición.
"""


def superposicion(lista, otra_lista):
    if lista > otra_lista:
        lista_uno = lista
        lista_dos = otra_lista
        columnas = len(lista)
    else:
        lista_uno = otra_lista
        lista_dos = lista
        columnas = len(otra_lista)
    listas = [lista_uno] + [lista_dos]
    i = 0
    grado = 0
    n = 0
    car = []
    n = 0
    while n < len(lista_dos) and i < columnas:
        if listas[0][i] == listas[1][n]:
            grado = grado + 1
            car.append(i)
            n = n + 1
            i = i + 1    
        else:
            i = i + 1
    posicion = es_minimo(car)
    return posicion


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva'
    del ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    listas = list(input("ingrese lista"))
    otra = list(input("ingrese otra lista"))
    superpuestos = superposicion(listas, otra)
    print(f"Posicion de inicio de superposicion")
    
if __name__ == "__main__":
    principal()
