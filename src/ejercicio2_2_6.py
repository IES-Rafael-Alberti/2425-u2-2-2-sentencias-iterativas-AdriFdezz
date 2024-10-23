"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""

def leerAltura() -> int:
    """
    Lee un numero entero del usuario para obtener la altura.

    Returns:
        int: El numero entero introducido por el usuario.
    """
    numeroValido = False
    numero = 0

    while not numeroValido:
        entrada = input("Introduce un numero entero positivo para saber la altura del triangulo: ")
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


def mostrarTriangulo(altura: int):
    """
    Muestra un triangulo rectangulo de la altura especificada.

    Args:
        altura (int): La altura del triangulo.
    """
    for nivel in range(1, altura + 1):
        print("*" * nivel)


def main():
    # Entrada
    altura = leerAltura()

    # Procesamiento
    # No lo veo necesario

    # Salida
    mostrarTriangulo(altura)


if __name__ == '__main__':
    main()