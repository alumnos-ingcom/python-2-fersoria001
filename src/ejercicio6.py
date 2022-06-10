################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 6. El Cifrado del Cesar
El cifrado César o cifrado de rotación usa una encriptación de 
sustitución simple. Esto significa que cada caracter se sustituye 
por otro caracter de acuerdo con un sistema especifico. 

La codificación debe ser tal que la palabra codificada contenga 
unicamente caracteres del tipo AZaz y 0 a 9, de manera que al 
codificar las ultimas letras del abecedario se vuelva a las primeras letras.

**Por ejemplo**, el método conocido y muy utilizado ROT13 rota 
el alfabeto con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.

* Implementar una funcion que codifique un texto rotandolo 
una cantidad de posiciones ajustable.

* Implementar la funcion que decodifique el texto rotado una 
cantidad de posiciones ajustable.

Una buena forma para verificar este ejercicio es codificar y 
decodificar un texto y compararlo con lo que fué ingresado originalmente.

**Tip**: Implementar las funciones utilizando las funciones `ord` y `chr`.
"""

def cifrado_del_cesar(cadena):
    """ Esta funcion se encarga de codificar una cadena de texto
    rotando el alfabeto 13 posiciones hacia adelante:
    Precondiciones: Ingresar una cadena de texto
    Postcondiciones: Se regresa una cadena rotando codificada"""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
    rango_alfabeto= len(alfabeto)
    cifrado = ''
    limite = 65
    for letra in cadena:
        if not letra.isalpha():
            if letra.lower() == 'ñ':
                cifrado = cifrado + letra
            elif letra.lower() == ' ':
                cifrado = cifrado + letra
                continue
        unicode = ord(letra)
        alfa = alfabeto
        if letra.islower():
            alfa = alfabeto_min
            limite = 97
        posicion = (unicode - limite + 13) % rango_alfabeto
        cifrado = cifrado + alfa[posicion]
    return cifrado


def descifrado_del_cesar(cadena):
        """ Esta funcion se encarga de decodificar una cadena de texto
    rotando el alfabeto 13 posiciones hacia atras:
    Precondiciones: Ingresar una cadena de texto codificada en cesarROT13
    Postcondiciones: Se regresa una cadena decodificada"""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
    rango_alfabeto= len(alfabeto)
    descifrado = ''
    limite = 65
    for letra in cadena:
        if  letra.isalpha() is False:
            if letra.lower() == 'ñ':
                descifrado = descifrado + letra
            elif letra.lower() == ' ':
                descifrado = descifrado + letra
                continue
        unicode = ord(letra)
        alfa = alfabeto
        if letra.islower():
            alfa = alfabeto_min
            limite = 97
        posicion = (unicode - limite - 13) % rango_alfabeto
        descifrado = descifrado + alfa[posicion]
    return descifrado
        

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("ingrese un texto: ")
    cifrado = cifrado_del_cesar(cadena)
    descifrado = descifrado_del_cesar(cifrado)
    print(cifrado)
    print(descifrado)


if __name__ == "__main__":
    principal()
