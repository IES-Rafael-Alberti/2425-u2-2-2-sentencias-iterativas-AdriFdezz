"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
"""

def leerNumero() -> int:
    """
    Lee un numero entero del usuario.

    Returns:
        int: El numero entero introducido por el usuario.
    """
    numeroValido = False
    numero = 0

    while not numeroValido:
        entrada = input("Introduce un numero entero (0 para terminar): ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                numero = int(entrada)
                if numero < 0:
                    print("Error: Debes introducir un numero entero positivo o 0 para terminar.")
                else:
                    numeroValido = True
        except ValueError:
            print("Error: Debes introducir un numero entero valido.")
    
    return numero

def obtenerNumeros() -> list:
    """
    Obtiene una lista de numeros enteros positivos del usuario hasta que se ingrese 0.

    Returns:
        list: Lista de numeros ingresados por el usuario.
    """
    numeros = []
    numero = None

    while numero != 0:
        numero = leerNumero()
        if numero > 0:
            numeros.append(numero)
    
    return numeros

def procesarNumeros(numeros: list) -> int:
    """
    Procesa los numeros ingresados y retorna la sumatoria.

    Args:
        numeros (list): Lista de numeros enteros.

    Returns:
        int: La sumatoria de los numeros ingresados.
    """
    return sum(numeros)

def mostrarResultado(suma: int):
    """
    Muestra la sumatoria de los numeros ingresados.

    Args:
        suma (int): La sumatoria de los numeros.
    """
    print("La sumatoria de los numeros positivos ingresados es: " + str(suma))

def main():
    # Entrada
    numeros = obtenerNumeros()

    # Procesamiento
    suma = procesarNumeros(numeros)

    # Salida
    mostrarResultado(suma)

if __name__ == '__main__':
    main()
