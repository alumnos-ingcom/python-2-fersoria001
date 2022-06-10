################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio2 import sumar, promediar

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
    secuencia = [15,62,-2]
    prueba = promediar(secuencia)
    interno = sum(secuencia) / len(secuencia)
    assert type(prueba) == float, "Requerimos resultado con decimales"
    assert prueba == interno, "Resultado incorrecto"
