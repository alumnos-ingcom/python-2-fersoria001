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
    """ Esta funcion se encarga de sumar una secuencia de numeros
    Precondiciones : Ingresar una lista de numeros
    Postcondiciones : se devuelve un numero float.
    """
    suma = 0
    i = 0
    rango = len(notas)
    try:
        while i < rango:
            notas[i] = float(notas[i])
            suma = suma + notas[i]
            i = i + 1
    except ValueError as exc:
        print("No ingresó una cadena de numeros: ", exc)
    return suma


def promediar(notas):
    """ Esta funcion obtiene el promedio de una secuencia de numeros
    Precondiciones: Ingresar una lista de numeros
    Postcondiciones: Se devuelve un numero float."""
    digitos = len(notas)
    notas = sumar(notas)
    promedio = notas / digitos
    return promedio


def es_maximo(notas):
    """ Esta funcion averigua el mayor numero de una secuencia.
    Precondiciones: Ingresar una lista de numeros
    Postcondiciones: Devuelve el mayor numero de la lista.
    """
    rango = len(notas)
    i = 0
    maximo = 0
    try:
        while i < rango:
            if notas[i] > maximo:
                maximo = notas[i]
            i = i + 1
    except TypeError as exce:
        print("No ingresó una cadena de numeros: \n ", exce)
    return maximo


def es_minimo(notas):
    """ Esta funcion averigua el menor numero de una secuencia.
    Precondiciones: Ingresar una lista de numeros
    Postcondiciones: Devuelve el menor numero de la lista.
    """
    rango = len(notas)
    i = 0
    minimo = notas[0]
    try:
        while i < rango:
            if notas[i] < minimo:
                minimo = notas[i]
            i = i + 1
    except TypeError as excep:
        print("No ingresó una cadena de numeros: ", excep)
    return minimo
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    notas = input("ingrese una secuencia de numeros separados: ")
    try:
        notas = notas.split()
        suma = sumar(notas)
        promedio = promediar(notas)
        mayor = es_maximo(notas)
        menor = es_minimo(notas)
    except ValueError as exc:
        ("Ingrese una secuencia de numeros separados")
    print(f"suma, promedio, mayor, menor {(suma, promedio, mayor, menor)}")
    


if __name__ == "__main__":
    principal()
