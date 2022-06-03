################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio
de una secuencia con números, retornando los valores como una `tuple`.
Sin utilizar lazos `for` o las funciones integradas del lenguaje
que procesan secuencias.
"""


def suma(notas):
    suma = 0
    rango = len(notas)
    i = 0
    while i < rango:
        notas[i] = int(notas[i])
        suma = suma + notas[i]
        i = i + 1
    return suma


def promedio(notas):
    digitos = len(notas)
    notas = suma(notas)
    promedio = notas / digitos
    return promedio


def maximos(notas):
    
    


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    numeros = int(input("Ingrese una lista"))
    invocacion = suma(numeros)
    print(f" Es el {numeros} par? : {invocacion}")


if __name__ == "__main__":
    principal()

