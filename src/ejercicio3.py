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

cadena = "Hola Mundo"
otra_cadena = "Hola"
lista_uno = list(cadena)
lista_dos = list(otra_cadena)
if lista_uno < lista_dos:
    rango = len(lista_uno)
else:
    rango = len(lista_dos)
i = 0
car = []
while i < rango:
    if lista_uno[i] == lista_dos[i]:
        car.append(lista_uno[i])
        i = i + 1
print(car)

    


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

