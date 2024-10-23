"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

"""

def leerNumero() -> int:
    """
    Lee un numero entero positivo del usuario.

    Returns:
        int: El numero entero positivo introducido por el usuario.
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
                    print("Error: Debes introducir un numero positivo.")
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

def mostrarResultado(suma: int):
    """
    Muestra la suma de los digitos del numero.

    Args:
        suma (int): La suma de los digitos del numero.
    """
    print("La suma de los digitos es: " + str(suma))

def main():
    # Entrada
    numero = leerNumero()

    # Procesamiento
    suma = sumarDigitos(numero)

    # Salida
    mostrarResultado(suma)

if __name__ == '__main__':
    main()
