"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

"""

def leerNumero() -> int:
    """
    Lee un numero entero positivo del usuario. La condicion de corte es -1.

    Returns:
        int: El numero entero introducido por el usuario.
    """
    numeroValido = False
    numero = 0

    while not numeroValido:
        entrada = input("Introduce un numero entero positivo (-1 para terminar): ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                numero = int(entrada)
                if numero < -1:
                    print("Error: Debes introducir un numero positivo o -1 para terminar.")
                else:
                    numeroValido = True
        except ValueError:
            print("Error: Debes introducir un numero entero valido.")
    
    return numero

def sumarDigitos(numero: int) -> int:
    """
    Calcula la suma de los digitos de un numero entero positivo.

    Args:
        numero (int): El numero entero positivo.

    Returns:
        int: La suma de los digitos del numero.
    """
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

def contarPares(numeros: list) -> int:
    """
    Cuenta cuantos de los numeros en la lista son pares.

    Args:
        numeros (list): Lista de numeros enteros.

    Returns:
        int: La cantidad de numeros pares.
    """
    pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
    return pares

def mostrarResultado(suma: int):
    """
    Muestra la suma de los digitos del numero.

    Args:
        suma (int): La suma de los digitos del numero.
    """
    print("La suma de los digitos es: " + str(suma))

def mostrarCantidadPares(cantidadPares: int):
    """
    Muestra la cantidad de numeros pares ingresados.

    Args:
        cantidadPares (int): La cantidad de numeros pares.
    """
    print("La cantidad de numeros pares ingresados es: " + str(cantidadPares))

def procesarNumeros():
    """
    Procesa los numeros ingresados, sumando los digitos y contando los pares.
    """
    numeros = []
    numero = leerNumero()

    while numero != -1:
        numeros.append(numero)
        suma = sumarDigitos(numero)
        mostrarResultado(suma)
        numero = leerNumero()

    return numeros

def main():
    # Entrada
    numeros = procesarNumeros()

    # Procesamiento
    cantidadPares = contarPares(numeros)

    # Salida
    mostrarCantidadPares(cantidadPares)

if __name__ == '__main__':
    main()
