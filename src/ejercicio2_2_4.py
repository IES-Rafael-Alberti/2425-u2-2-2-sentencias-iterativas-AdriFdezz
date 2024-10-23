"""
Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.
"""

def leerNumero() -> int:
    """
    Lee un numero entero positivo del usuario.

    Si el numero no es un numero entero valido o es menor o igual a cero, mostrara un mensaje de error y volvera a pedir el numero.

    Returns:
        int: El numero introducido por el usuario.
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

def cuentaAtras(numero: int) -> list:
    """
    Genera una lista con la cuenta atras desde el numero especificado hasta cero.

    Args:
        numero (int): El numero desde el cual se realizara la cuenta atras.

    Returns:
        list: Lista de numeros desde el numero dado hasta cero.
    """

    return list(range(numero, -1, -1))

def mostrarResultado(cuenta: list):
    """
    Muestra por pantalla la cuenta atras separados por comas.

    Args:
        cuenta (list): Lista de numeros de la cuenta atras.
    """

    print("Cuenta atras:", ", ".join(str(numero) for numero in cuenta))

def main():
    # Entrada
    numero = leerNumero()

    # Procesamiento
    cuenta = cuentaAtras(numero)

    # Salida
    mostrarResultado(cuenta)

if __name__ == '__main__':
    main()
