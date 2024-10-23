"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

def leerEntrada() -> str:
    """
    Lee la entrada del usuario.

    Returns:
        str: La entrada introducida por el usuario.
    """
    entrada = input("Introduce algo (escribe 'salir' para terminar): ")
    return entrada

def mostrarEco(entrada: str):
    """
    Muestra el eco de la entrada del usuario.

    Args:
        entrada (str): La entrada introducida por el usuario.
    """
    print(entrada)

def procesarEntrada():
    """
    Procesa la entrada del usuario hasta que se deba terminar.
    """
    entrada = leerEntrada()
    while entrada.lower() != "salir":
        mostrarEco(entrada)
        entrada = leerEntrada()

def main():
    # Entrada/Procesado/Salida
    # No se muy bien como separar esto
    procesarEntrada()

if __name__ == '__main__':
    main()

