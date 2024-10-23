"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

def leerFrase() -> str:
    """
    Lee una frase del usuario.

    Returns:
        str: La frase introducida por el usuario.
    """
    fraseValida = False
    frase = ""

    while not fraseValida:
        entrada = input("Introduce una frase: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            elif any(letra.isdigit() for letra in entrada):
                print("Error: La entrada no puede contener numeros.")
            else:
                frase = entrada
                fraseValida = True
        except ValueError:
            print("Error: Debes introducir una frase valida.")

    return frase

def leerLetra() -> str:
    """
    Lee una letra del usuario. Si la entrada no es un solo caracter, muestra un mensaje de error
    y vuelve a pedir la letra.

    Returns:
        str: La letra introducida por el usuario.
    """
    letraValida = False
    letra = ""

    while not letraValida:
        entrada = input("Introduce una letra: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            elif len(entrada) != 1:
                print("Error: Debes introducir solo una letra.")
            elif any(letra.isdigit() for letra in entrada):
                print("Error: La entrada no puede contener numeros.")
            else:
                letra = entrada
                letraValida = True
        except ValueError:
            print("Error: Debes introducir una letra valida.")

    return letra

def contarLetras(frase: str, letra: str) -> int:
    """
    Cuenta el numero de veces que una letra aparece en una frase.

    Args:
        frase (str): La frase en la que se buscara la letra.
        letra (str): La letra que se contara en la frase.

    Returns:
        int: El numero de veces que aparece la letra en la frase.
    """
    return frase.count(letra)

def mostrarResultado(letra: str, cantidad: int):
    """
    Muestra el resultado del conteo de letras.

    Args:
        letra (str): La letra que se ha contado.
        cantidad (int): El numero de veces que aparece la letra en la frase.
    """
    print("La letra '" + letra + "' aparece " + str(cantidad) + " veces en la frase.")

def main():
    # Entrada
    frase = leerFrase()
    letra = leerLetra()

    # Procesamiento
    cantidad = contarLetras(frase, letra)

    # Salida
    mostrarResultado(letra, cantidad)

if __name__ == '__main__':
    main()

