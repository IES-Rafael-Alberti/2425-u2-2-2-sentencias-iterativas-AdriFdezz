"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

def leerPalabra() -> str:
    """
    Lee una palabra del usuario. Si la palabra está vacia, muestra un mensaje de error
    y vuelve a pedir la palabra.

    Returns:
        str: La palabra introducida por el usuario.
    """
    palabraValida = False
    palabra = ""

    while not palabraValida:
        entrada = input("Introduce una palabra: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                palabra = entrada
                palabraValida = True
        except ValueError:
            print("Error: Debes introducir una palabra valida.")

    return palabra

def procesarPalabra(palabra: str) -> list:
    """
    Procesa la palabra y retorna una lista de letras en orden inverso.

    Args:
        palabra (str): La palabra que se va a procesar.

    Returns:
        list: Lista de letras de la palabra en orden inverso.
    """
    letrasInversas = []
    longitud = len(palabra)
    for indice in range(longitud - 1, -1, -1):
        letrasInversas.append(palabra[indice])
    
    return letrasInversas

def mostrarResultado(letras: list):
    """
    Muestra por pantalla las letras de la palabra en orden inverso.

    Args:
        letras (list): Lista de letras en orden inverso.
    """
    for letra in letras:
        print(letra)

def main():
    # Entrada
    palabra = leerPalabra()

    # Procesamiento
    letrasInversas = procesarPalabra(palabra)

    # Salida
    mostrarResultado(letrasInversas)

if __name__ == '__main__':
    main()
