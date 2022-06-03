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
    notas = []
    i = int(input("Cuantos valores tiene su secuencia de numeros?: "))
    while i  > 0:
        numero = float(input("ingrese un numero: "))
        notas.append(numero)
        i  = i - 1
    suma = sumar(notas)
    promedio = promediar(notas)
    mayor = es_maximo(notas)
    menor = es_minimo(notas)
    print(f"suma, promedio, mayor, menor {(suma, promedio, mayor, menor)}")
    


if __name__ == "__main__":
    principal()
