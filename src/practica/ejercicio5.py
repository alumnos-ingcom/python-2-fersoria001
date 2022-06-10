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

def balanceados(cadena, signos):
    """ Esta funcion comprueba si los signos tienen su reciproco
    Precondiciones: Ingresar una cadena de texto y un par o mas de signos
    , estos ultimos sin separacion.
    Postcondiciones: Se devuelve un valor booleano True si estan todos
    los signos encuentran su reciproco y False si no.
    """
    simbolos = list()
    comparo = list()
    temporal = list()
    for signo in signos:
        simbolos.append(signo)
    for i in range(len(simbolos)):
        for letra in cadena:
            if letra in simbolos[i]:
                temporal.append(letra)
        comparo.append(temporal)
        temporal = []
    rango = len(comparo)
    for i in range(rango):
        for j in range(i+1, rango):
            resultado = len(comparo[i]) == len(comparo[j])
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    simbolos = input("ingrese parejas de signos sin ninguna separacion")
    entrada = input("Ingrese una cadena para analizar")
    invoco = balanceados(entrada, simbolos)
    print(invoco)


if __name__ == "__main__":
    principal()
