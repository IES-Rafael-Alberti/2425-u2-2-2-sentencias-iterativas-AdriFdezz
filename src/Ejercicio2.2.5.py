"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""

def leerCantidad() -> float:
    """
    Lee la cantidad a invertir del usuario.

    Returns:
        float: La cantidad introducida por el usuario.
    """
    cantidadValida = False
    cantidad = 0.0

    while not cantidadValida:
        entrada = input("Introduce la cantidad a invertir: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                cantidad = float(entrada)
                if cantidad <= 0:
                    print("Error: La cantidad debe ser un numero positivo.")
                else:
                    cantidadValida = True
        except ValueError:
            print("Error: Debes introducir un numero valido.")

    return cantidad


def leerInteres() -> float:
    """
    Lee el interes anual del usuario.

    Returns:
        float: El interes anual introducido por el usuario.
    """
    interesValido = False
    interes = -1.0

    while not interesValido:
        entrada = input("Introduce el interes anual (%): ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                interes = float(entrada)
                if interes < 0:
                    print("Error: El interes no puede ser negativo.")
                else:
                    interesValido = True
        except ValueError:
            print("Error: Debes introducir un numero valido.")

    return interes


def leerAnios() -> int:
    """
    Lee el numero de años de inversion del usuario.

    Returns:
        int: El numero de años introducido por el usuario.
    """
    aniosValido = False
    anios = 0

    while not aniosValido:
        entrada = input("Introduce el numero de años de inversion: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                anios = int(entrada)
                if anios <= 0:
                    print("Error: El numero de años debe ser un numero positivo.")
                else:
                    aniosValido = True
        except ValueError:
            print("Error: Debes introducir un numero entero valido.")

    return anios


def calcularInversion(cantidad: float, interes: float, anios: int) -> list:
    """
    Calcula el capital obtenido en la inversion cada año.

    Args:
        cantidad (float): La cantidad a invertir.
        interes (float): El interes anual.
        anios (int): El numero de años de inversion.

    Returns:
        list: Lista de capital obtenido en cada año.
    """
    capitalPorAnio = []
    for anio in range(1, anios + 1):
        cantidad *= 1 + interes / 100
        capitalPorAnio.append(round(cantidad, 2))

    return capitalPorAnio


def mostrarResultado(capital: list):
    """
    Muestra por pantalla el capital obtenido cada año.

    Args:
        capital (list): Lista de capital obtenido cada año.
    """
    for anio, monto in enumerate(capital, start=1):
        print("Año:", anio, " Capital obtenido:", monto)


def main():
    # Entrada
    cantidad = leerCantidad()
    interes = leerInteres()
    anios = leerAnios()

    # Procesamiento
    capital = calcularInversion(cantidad, interes, anios)

    # Salida
    mostrarResultado(capital)


if __name__ == '__main__':
    main()
