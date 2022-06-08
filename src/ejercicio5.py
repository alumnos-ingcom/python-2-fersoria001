################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 5. Corchetes balanceados
Implementar una función que determine si una cadena con corchetes 
está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. 
El resultado debe ser un valor lógico indicando si esta o no balanceado.

**Ejemplos**
```
   (vacio)      True
   []           True
   [][]         True
   [[][]]       True
   ][           False
   ][][         False
   []][[]       False
```
La funcion deberia de ignorar todo lo que no sean corchetes.

#### Extra #1
Hacer que la funcion reciba _que_ par de simbolos buscar si esta 
balanceado. (como para pasar parentesis, llaves o cualquier otro)

#### Extra #2
Hacer que la función verifique el balanceo simultaneo de parentesis, 
llaves y corchetes.
"""

def balanceados(cadena, tipo):
    simbolo = list()
    for car in tipo:
        simbolo.append(car)
    temporal = list()
    for car in cadena:
        if car in simbolo:
            temporal.append(car)
    resultado = len(temporal) % 2 == 0
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    simbolos = input("Ingrese el par de simbolos a comprobar")
    entrada = list(input("Ingrese una cadena"))
    invoco = balanceados(entrada, simbolos)
    print(invoco)


if __name__ == "__main__":
    principal()
