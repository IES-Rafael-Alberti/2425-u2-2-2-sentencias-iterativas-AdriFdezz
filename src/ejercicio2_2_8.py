"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

def leerNumero() -> int:
    """
    Lee un numero entero positivo del usuario.

    Si la entrada es vacia o no es un numero entero positivo, mostrara un mensaje de error y volvera a pedir el numero.

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
                    print("Error: Debes introducir un numero positivo.")
                else:
                    numeroValido = True
        except ValueError:
            print("Error: Debes introducir un numero entero valido.")

    return numero


def generarTriangulo(numero: int) -> list:
    """
    Genera un triangulo rectangulo.

    Args:
        numero (int): La altura del triangulo.

    Returns:
        list: Una lista de listas, donde cada lista contiene los numeros de cada fila del triangulo.
    """
    triangulo = []
    for fila in range(1, numero + 1):
        numeros = []
        for valor in range(1, fila + 1):
            numeros.append(2 * valor - 1)
        triangulo.append(numeros[::-1])
    return triangulo


def mostrarTriangulo(triangulo: list):
    """
    Muestra el triangulo rectangulo en la pantalla.

    Args:
        triangulo (list): Una lista de listas que contiene los numeros del triangulo.
    """
    for fila in triangulo:
        almacenarNumerosFila = ""
        for numero in fila:
            almacenarNumerosFila += str(numero) + " "
        print(almacenarNumerosFila.strip())


def main():
    # Entrada
    numero = leerNumero()

    # Procesamiento
    triangulo = generarTriangulo(numero)

    # Salida
    mostrarTriangulo(triangulo)


if __name__ == '__main__':
    main()
