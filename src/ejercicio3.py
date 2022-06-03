################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

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


def superposicion(cadena, otra_cadena):
    lista_uno = list(cadena)
    lista_dos = list(otra_cadena)
    listas = [lista_uno] + [lista_dos]
    if lista_uno > lista_dos:
        columnas = len(lista_uno)
    else:
        columnas = len(lista_dos)
    filas = len(listas)
    i = 0
    grado = 0
    n = 0
    while i < columnas:
        while n < len(lista_dos):
            if listas[0][i] == listas[1][n]:
                grado = grado + 1
            n = n + 1
        i = i + 1
        n = 0
    return grado


    


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva'
    del ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("ingrese cadena")
    otra = input("ingrese otra cadena")
    superpuestos = superposicion(cadena, otra)
    print(superpuestos)
    
if __name__ == "__main__":
    principal()

