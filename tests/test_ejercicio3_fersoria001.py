"""
Se probara si el superposicionador puede devolver el grado de
superposicion de dos listas y su posicion de inicio de superposicion
"""
################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio3 import superposicion

def test_superposicion_true_uno():
    """
    Se otorgan dos listas con valores arbitrarios de superposicion
    con la primer lista de mayor rango que la segunda
    """
    lista = list("Hola Mundo")
    otra_lista = list("Hola")
    prueba = superposicion(lista, otra_lista)
    grado = 4
    inicio = 0
    assert prueba == (grado, inicio), "Resultado incorrecto"


def test_superposicion_true_dos():
    """
    Se otorgan dos listas con valores arbitrarios de superposicion
    con la primer lista de menor rango que la segunda
    """
    lista = list("Hola")
    otra_lista = list("Hola Mundo")
    prueba = superposicion(lista, otra_lista)
    grado = 4
    inicio = 0
    assert prueba == (grado, inicio), "Resultado incorrecto"


def test_superposicion_false():
    """
    Se otorgan dos listas con valores arbitrarios de superposicion
    con la primer lista de mayor rango que la segunda y sin superposicion
    """
    lista = list("Hola Mundo")
    otra_lista = list("Fercho")
    prueba = superposicion(lista, otra_lista)
    grado = 0
    inicio = None
    assert prueba == (grado, inicio), "Resultado incorrecto"

def test_superposicion_true_tres():
    """
    Se otorgan dos listas con valores arbitrarios de superposicion
    con la primer lista de mayor rango que la segunda
    """
    lista = list("fercho Hola Mundo todo ok")
    otra_lista = list("Hola Mundo")
    prueba = superposicion(lista, otra_lista)
    grado = 10
    inicio = 7
    assert prueba == (grado, inicio), "Resultado incorrecto"
