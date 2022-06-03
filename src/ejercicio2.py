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


def acondicionar_secuencia(secuencia):
    """ Esta funcion quita comas y espacios de un string
    Precondicion: ingresar un string
    Postcondicion: devuelve una lista de caracteres
    """
    secuencia = secuencia.replace(",", "")
    secuencia = secuencia.replace(" ", "")
    secuencia = list(secuencia)
    rango = len(secuencia)
    i = 0
    while i < rango:
        secuencia[i] = int(secuencia[i])
        secuencia[i] = float(secuencia[i])
        i = i + 1
    return secuencia


def sumar(notas):
    suma = 0
    notas = acondicionar_secuencia(notas)
    rango = len(notas)
    i = 0
    while i < rango:
#        notas[i] = int(notas[i])
#        notas[i] = float(notas[i])
        suma = suma + notas[i]
        i = i + 1
    return suma


def promediar(notas):
    digitos = len(notas)
    notas = sumar(notas)
    promedio = notas / digitos
    return promedio


def maximos(notas):
    notas = sacar_comas(notas)
    rango = len(notas)
    i = 0
    maximo = 0
    while i < rango:
        if notas[i] > maximo:
            maximo = notas[i]
        i = i + 1
    return maximo


def minimos(notas):
    notas = acondicionar_secuencia(notas)
    rango = len(notas)
    i = 0
    while i < rango:
        if notas[i] < notas[-i]:
            minimo = notas[i]
        i = i + 1
    return minimo
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    numeros = input("Ingrese una lista")
    suma = sumar(numeros)
    promedios = promediar(numeros)
    print(f" promedios {promedios} , suma{suma}")


if __name__ == "__main__":
    principal()

