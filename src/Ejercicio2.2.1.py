"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def leerPalabra() -> str:
    """
    Lee una palabra del usuario.

    Si la palabra esta vacia, mostrara un mensaje de error y volvera a pedir la palabra.

    Returns:
        str: La palabra introducida por el usuario.
    """

    palabraValida = False
    palabra = ""

    while not palabraValida:
        palabra = input("Introduce una palabra: ")
        
        if palabra.strip() == "":
            print("Error: La palabra no puede estar vacia.")
        else:
            palabraValida = True

    return palabra

def repetirPalabra(palabra: str) -> str:
    """
    Repite la palabra 10 veces.

    Args:
        palabra (str): La palabra a repetir.

    Returns:
        str: La cadena con la palabra repetida 10 veces.
    """

    resultado = ""

    for repetir in range(10):
        resultado += palabra + " "

    return resultado

def mostrarResultado(resultado: str):
    """
    Muestra por pantalla el resultado.

    Args:
        resultado (str): La cadena con la palabra repetida.
    """

    print (resultado)

def main():
    #Entrada
    palabra = leerPalabra()

    #Procesamiento
    resultado = repetirPalabra(palabra)

    #Salida
    mostrarResultado(resultado)

if __name__ == '__main__':
    main()