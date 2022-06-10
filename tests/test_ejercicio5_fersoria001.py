################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio5 import balanceados

"""
Se probará en este archivo la funcion para comprobar si una cadena
de simbolos esta balanceada o no
"""


def test_balanceados_corchetes_true():
    """
    Probaremos si una cadena de corchetes esta balanceada
    """
    cadena = "[ ] [] [] ]["
    simbolos = "[]"
    llamo = balanceados(cadena, simbolos)
    assert llamo == True, "Resultado incorrecto"
    assert type(llamo) == bool, "Tipo de resultado incorrecto"


def test_balanceados_corchetes_false():
    """
    Probaremos si una cadena de corchetes esta balanceada
    """
    cadena = "[ ] ] []]"
    simbolos = "[]"
    llamo = balanceados(cadena, simbolos)
    assert llamo == False, "Resultado incorrecto"
    assert type(llamo) == bool, "Tipo de resultado incorrecto"


def test_balanceados_parentesis_false():
    """
    Probaremos si una cadena de parentesis esta balanceada con
    resultado false
    """
    cadena = "( ) (() )("
    simbolos = "()"
    llamo = balanceados(cadena, simbolos)
    assert llamo == False, "Resultado incorrecto"
    assert type(llamo) == bool, "Tipo de resultado incorrecto"


def test_balanceados_parentesis_true():
    """
    Probaremos si una cadena de parentesis esta balanceada con resultado
    true
    """
    cadena = "( ) (() )()"
    simbolos = "()"
    llamo = balanceados(cadena, simbolos)
    assert llamo == True, "Resultado incorrecto"
    assert type(llamo) == bool, "Tipo de resultado incorrecto"


def test_balanceados_todos_true():
    """
    Probaremos si una cadena tiene sus signos  balanceados con resultado
    true
    """
    cadena = "( ) (() )() [][] ]] [[ { } {{}} }{"
    simbolos = "()[]{}"
    llamo = balanceados(cadena, simbolos)
    assert llamo == True, "Resultado incorrecto"
    assert type(llamo) == bool, "Tipo de resultado incorrecto"

def test_balanceados_todos_false():
    """
    Probaremos si una cadena tiene sus signos  balanceados
    con resultado false
    """
    cadena = "( ) (() )() [][] ]] [[ { } {{}} }"
    simbolos = "()[]{}"
    llamo = balanceados(cadena, simbolos)
    assert llamo == False, "Resultado incorrecto"
    assert type(llamo) == bool, "Tipo de resultado incorrecto"