################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
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
    cadena = list(cadena)
    otra_cadena = list(otra_cadena)
    if len(cadena) > len(otra_cadena):
        rango = len(cadena)
    else:
        rango = len(otra_cadena)  
    i = 0
    grado = 0
    while i < rango: 
        if cadena[i] == otra_cadena[i]:
            grado = grado + 1
        i = i + 1
    return grado
    


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("ingrese cadena")
    otra = input("ingrese otra cadena")
    superpuestos = superposicion(cadena, otra)
    print(superpuestos)
    
if __name__ == "__main__":
    principal()

