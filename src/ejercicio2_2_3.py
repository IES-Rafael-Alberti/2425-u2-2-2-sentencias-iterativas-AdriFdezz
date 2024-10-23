"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""

def leerNumero() -> int:
    """
    Lee un numero entero positivo del usuario.

    Si el numero no es un numero entero valido o es menor o igual a cero, mostrara un mensaje de error y volvera a pedir el numero.

    Returns:
        int: El número introducido por el usuario.
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

def numerosImpares(numero: int) -> list:
    """
    Genera una lista de numeros impares desde 1 hasta el numero introducido.

    Args:
        numero (int): El numero hasta el cual se generaran los impares.

    Returns:
        list: Lista de numeros impares.
    """

    listaImpares = []
    for numeroActual in range(1, numero + 1):
        if numeroActual % 2 != 0:
            listaImpares.append(numeroActual)

    return listaImpares

def mostrarResultado(impares: list):
    """
    Muestra por pantalla todos los numeros impares separados por comas.

    Args:
        impares (list): Lista de numeros impares.
    """

    print("Numeros impares:", ", ".join(str(numero) for numero in impares))

def main():
    # Entrada
    numero = leerNumero()

    # Procesamiento
    impares = numerosImpares(numero)

    # Salida
    mostrarResultado(impares)

if __name__ == '__main__':
    main()
