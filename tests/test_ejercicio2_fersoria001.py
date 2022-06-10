################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio2 import sumar, promediar, es_maximo, es_minimo

"""
Aqui se probaran las funciones correspondientes al ejercicio2
comparando resultados con funciones internas en lo posible.
"""


def test_sumar():
    """
    Se intentará sumar una secuencia de numeros ingresada y retornar
    un resultado tipo float
    """
    secuencia = [1,2,10,15]
    prueba = sumar(secuencia)
    interno = sum(secuencia)
    assert type(prueba) == float, "Tipo incorrecto de resultado"
    assert prueba == interno, "Suma incorrecta"


def test_promediar():
    """
    Se intentará promediar una secuencia de numeros ingresada y retornar
    un resultado tipo float
    """
    secuencia = [15,62,-2]
    prueba = promediar(secuencia)
    interno = sum(secuencia) / len(secuencia)
    assert type(prueba) == float, "Requerimos resultado con decimales"
    assert prueba == interno, "Resultado incorrecto"


def test_es_maximo():
    """
    Se buscará el numero mayor de una secuencia de numeros ingresada
    y retornarlo
    """
    secuencia = [20, 32, -1, 1]
    prueba = es_maximo(secuencia)
    interno = max(secuencia)
    assert prueba == interno, "Resultado incorrecto"


def test_es_minimo():
    """
    Se buscará el numero menor de una secuencia de numeros ingresada
    y retornarlo
    """
    secuencia = [33,91,22,22]
    prueba = es_minimo(secuencia)
    interno = min(secuencia)
    assert prueba == interno, "Resultado incorrecto"
