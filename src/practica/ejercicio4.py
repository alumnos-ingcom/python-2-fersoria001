################
# Fernando Agustín Soria - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es
la suma de los dos anteriores. En la misma, los dos primeros términos
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""
def fibonacci(termino):
    """ Esta función comienza desde el tercer termino de fibonacci
    siendo los primeros dos 1,1 y utiliza la misma para obtener un numero.
    Precondiciones: Ingresar un numero entero positivo mayor a 2.
    Postcondicion: Retorna el n-esimo numero de la sucesión, teniendo en
    cuenta que comienza a contar desde el 2do termino"""
    contador = 2
    primer = 1
    segundo = 1
    while contador < termino:
        enesimo = primer + segundo
        primer = segundo
        segundo = enesimo
        contador = contador + 1
    return enesimo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print("Sucesion de Fibonacci: Comienza con 1,1 siendo estos \n"
              "los dos primeros terminos")
    try:
        termino = int(input("Ingrese el termino que desea obtener: "))
        if termino <= 2:
            raise ValueError("fuera de rango")
        invoco = fibonacci(termino)
        print(f"El  {termino} termino de esta sucesión de Fibonacci es {invoco}")
    except ValueError:
        print("Ingrese un numero entero positivo mayor a 2")


if __name__ == "__main__":
    principal()
