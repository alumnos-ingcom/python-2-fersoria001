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
    corchetes =  {"[", "]"}
    parentesis = {"(", ")"}
    llaves = {"{", "}"}
#    columnas = list()
    temporal = list()
    if tipo == 1:
        for car in cadena:
            if car in corchetes:
                temporal.append(car)
    elif tipo == 2:
        for car in cadena:
            if car in parentesis:
                temporal.append(car)
    elif tipo == 3:
        for car in cadena:
            if car in llaves:
                temporal.append(car)
#    else:
    resultado = len(temporal) % 2 == 0
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    simbolo = int(input("Verif (1) corchetes, (2) parentesis, (3) llaves"))
    entrada = list(input("Ingrese una cadena"))
    invoco = balanceados(entrada, simbolo)
    print(invoco)


if __name__ == "__main__":
    principal()
