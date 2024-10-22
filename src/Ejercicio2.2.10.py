"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

def leerNumeroEntero() -> int:
    """
    Lee un numero entero del usuario. Si la entrada es una cadena vacia o no es un numero válido,
    
    muestra un mensaje de error y vuelve a pedir el numero.

    Returns:
        int: El numero entero introducido por el usuario.
    """
    numeroValido = False
    numero = 0

    while not numeroValido:
        entrada = input("Introduce un numero entero positivo: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                numero = int(entrada)
                if numero <= 0:
                    print("Error: Debes introducir un numero entero positivo.")
                else:
                    numeroValido = True
        except ValueError:
            print("Error: Debes introducir un numero entero valido.")
    
    return numero

def esPrimo(numero: int) -> bool:
    """
    Determina si un numero es primo.

    Args:
        numero (int): El numero a verificar.

    Returns:
        bool: True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

def mostrarResultado(numero: int, primo: bool):
    """
    Muestra por pantalla si el numero es primo o no.

    Args:
        numero (int): El numero introducido por el usuario.
        primo (bool): True si el numero es primo, False en caso contrario.
    """
    if primo:
        print("El numero " + str(numero) + " es primo.")
    else:
        print("El numero " + str(numero) + " no es primo.")

def main():
    # Entrada
    numero = leerNumeroEntero()

    # Procesamiento
    primo = esPrimo(numero)

    # Salida
    mostrarResultado(numero, primo)

if __name__ == '__main__':
    main()