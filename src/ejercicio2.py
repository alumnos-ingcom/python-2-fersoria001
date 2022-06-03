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


def sumar(notas):
    suma = 0
    i = 0
    rango = len(notas)
    while i < rango:
        suma = suma + notas[i]
        i = i + 1
    return suma


def promediar(notas):
    digitos = len(notas)
    notas = sumar(notas)
    promedio = notas / digitos
    return promedio


def es_maximo(notas):
    rango = len(notas)
    i = 0
    maximo = 0
    while i < rango:
        if notas[i] > maximo:
            maximo = notas[i]
        i = i + 1
    return maximo


def es_minimo(notas):
    rango = len(notas)
    i = 0
    minimo = notas[0]
    while i < rango:
        if notas[i] < minimo:
            minimo = notas[i]
        i = i + 1
    return minimo
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    numeros = input("ingrese digitos separados por comas o espacios")
    invocacion_uno = promediar(numeros)
    invocacion_dos = es_minimo(numeros)
    invocacion_tres = es_maximo(numeros)
    tupla = (invocacion_uno, invocacion_dos, invocacion_tres)
    print(f" promedios, max,min : {tupla}")


if __name__ == "__main__":
    principal()
