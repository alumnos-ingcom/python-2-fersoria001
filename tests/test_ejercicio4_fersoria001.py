################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio4 import fibonacci

"""
Se probará en este archivo la función de sucesiones de fibonacci
obteniendo el n-esimo termino de la misma comenzando desde 2,
pues los dos primeros terminos son 1 1.
"""


def test_fibonacci():
    """
    Probaremos obtener el 17vo termino de la sucesion obtenido desde
    wikipedia.
    """
    llamo = fibonacci(17)
    termino = 1597
    assert llamo == termino, "Resultado incorrecto"
    assert type(llamo) == int, "Tipo incorrecto"
