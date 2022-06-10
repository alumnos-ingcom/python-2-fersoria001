################
# Fernando Agustín Soria - @fesoria001
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

def balanceados(cadena, simbolos):
    pares = simbolos.split(', ')
    temporal = []
    parcial = []
    resultado = False
    for i in range(len(pares)):
        simbolo = pares[i].split(' ')
        for caracter in cadena:
            if caracter in simbolo:
                temporal.append(caracter)
        parcial.append(temporal)
    for c in range(len(parcial)):
        verifico = len(parcial[c]) % 2 == 0
    if verifico is True:
        resultado = verifico
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    try:
        simbolos = input("Ingrese los signos separados por espacios y"
                                     "las parejas separadas por coma espacio"
                                    ",deje el final en blanco sin espacios")
        entrada = list(input("Ingrese una cadena para analizar"))
        pares = simbolos.split(' ')
        if len(pares) <= 1:
            raise IndexError("No utilizó la separación recomendada")
        invoco = balanceados(entrada, simbolos)
        print(invoco)
    except IndexError as exc:
        print(exc)


if __name__ == "__main__":
    principal()
