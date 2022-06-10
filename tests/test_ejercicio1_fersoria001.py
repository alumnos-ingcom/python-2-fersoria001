################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio1 import es_par

"""
Este archivo prueba los diferentes casos donde la funcion es_par(numero)
deberia funcionar correctamente
"""


def test_es_par_positivo_false():
    """
    Se utiliza un numero impar positivo y 
    Se compara el resultado contra una variable type bool que utiliza
    el resto de la division por 2 == 0, el resultado debe ser False
    """
    llamo = es_par(5)
    comparo = 5 % 2 == 0
    assert type(llamo) == bool, "Tipo de resultado incorrecto"
    assert llamo == comparo, "Resultado incorrecto"
    

def test_es_par_positivo_true():
    """
    Se utiliza un numero par positivo y 
    Se compara el resultado contra una variable type bool que utiliza
    el resto de la division por 2 == 0, el resultado debe ser True
    """
    llamo = es_par(36)
    comparo = 36 % 2 == 0
    assert type(llamo) == bool, "Tipo de resultado incorrecto"
    assert llamo == comparo, "Resultado incorrecto"


def test_es_par_negativo_false():
    """
    Se utiliza un numero impar negativo y 
    Se compara el resultado contra una variable type bool que utiliza
    el resto de la division por 2 == 0, el resultado debe ser False
    """
    llamo = es_par(-15)
    comparo = -15 % 2 == 0
    assert type(llamo) == bool, "Tipo de resultado incorrecto"
    assert llamo == comparo, "Resultado incorrecto"


def test_es_par_negativo_true():
    """
    Se utiliza un numero par negativo y 
    Se compara el resultado contra una variable type bool que utiliza
    el resto de la division por 2 == 0, el resultado debe ser True
    """
    llamo = es_par(-42)
    comparo = -42 % 2 == 0
    assert type(llamo) == bool, "Tipo de resultado incorrecto"
    assert llamo == comparo, "Resultado incorrecto"
