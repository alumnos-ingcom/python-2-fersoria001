################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio6 import cifrado_del_cesar, descifrado_del_cesar

"""
En este archivo se probará la función que cifra y la que descifra en
cifrado del cesar perteneciente al ejercicio6
"""


def test_cifrado_del_cesar_rot13():
    """
    En esta funcion testearé comparando las funciones entre ellas mismas
    con el valor de rotacion por defecto.
    """
    cadena = "hola me llamo fer me gustan las medialunas"
    cadena_dos = "A N"
    cadena_tres = "N A"
    cifro = cifrado_del_cesar(cadena)
    descifro = descifrado_del_cesar(cifro)
    pruebo = cifrado_del_cesar(cadena_dos)
    compruebo = descifrado_del_cesar(pruebo)
    assert descifro == cadena, "Hubo algun error en la reconversion"
    assert pruebo == cadena_tres, "Hubo algun error en el cifrado"
    assert compruebo == cadena_dos, "Hubo algun error en el descifrado"
