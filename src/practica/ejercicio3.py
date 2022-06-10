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


def superposicion(lista, otra_lista):
    """ Esta función compara dos listas e indica si estan superpuestas.
    Precondiciones: Ingresar dos listas
    Postcondiciones: Se devuelve una tupla con el grado de superposicion
    y la posicion de inicio de la misma"""
    if lista > otra_lista:
        lista_mayor = lista
        lista_menor = otra_lista
    else:
        lista_mayor = otra_lista
        lista_menor = lista
    columnas = len(lista_mayor)
    listas = [lista_mayor] + [lista_menor]
    i = 0
    grado = 0
    j = 0
    car = []
    while j < len(lista_menor) and i < columnas:
        if listas[0][i] == listas[1][j]:
            grado = grado + 1
            car.append(i)
            j = j + 1
            i = i + 1
        else:
            grado = 0
            i = i + 1
    try:
        inicio = car[0]
    except IndexError as exc:
        print("No hay superposicion", exc)
        inicio = None
    return grado, inicio


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva'
    del ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    listas = list(input("ingrese lista"))
    otra = list(input("ingrese otra lista"))
    superpuestos = superposicion(listas, otra)
    print(superpuestos)
if __name__ == "__main__":
    principal()
