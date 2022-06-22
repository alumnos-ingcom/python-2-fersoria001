################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 1. Pares e impares
Escribir una función que retorne `True` cuando un número entero es par
y `False` cuando no lo sea, sin utilizar módulo. (`%`)
"""


def es_par(numero):
    """ Esta función sirve para averiguar si un numero es par o impar
    sin utilizar módulo.
    Precondición: Debe ingresar un numero tipo int
    Postcondicion: Se retorna un valor booleano.
    """
    if numero > 0:
        while numero >= 2:
            numero = numero - 2
    else:
        while numero <= -2:
            numero = numero + 2
    par = numero == 0
    return par


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    numeros = int(input("Ingrese un numero entero"))
    invocacion = es_par(numeros)
    print(f" Es el {numeros} par? : {invocacion}")


if __name__ == "__main__":
    principal()
