"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""

def leerNumero() -> int:
    """
    Lee un numero entero positivo del usuario.

    Returns:
        int: El numero entero introducido por el usuario.
    """
    numeroValido = False
    numero = 0

    while not numeroValido:
        entrada = input("Introduce un numero entero positivo (0 para terminar): ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                numero = int(entrada)
                if numero < 0:
                    print("Error: Debes introducir un numero positivo.")
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
        if numero != 0:
            numeros.append(numero)
    
    return numeros

def encontrarMayor(numeros: list) -> int:
    """
    Encuentra el mayor numero en una lista de numeros positivos.

    Args:
        numeros (list): Lista de numeros enteros positivos.

    Returns:
        int: El mayor numero de la lista.
    """
    if not numeros:
        return 0
    
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    
    return mayor

def mostrarResultado(mayor: int):
    """
    Muestra el mayor numero ingresado.

    Args:
        mayor (int): El mayor numero encontrado.
    """
    print("El mayor numero ingresado es: " + str(mayor))

def main():
    # Entrada
    numeros = obtenerNumeros()

    # Procesamiento
    mayor = encontrarMayor(numeros)

    # Salida
    mostrarResultado(mayor)

if __name__ == '__main__':
    main()

