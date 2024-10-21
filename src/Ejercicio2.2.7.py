"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

def calcularTablaMultiplicar():
    """
    Calcula la tabla de multiplicar del 1 al 10.

    Returns:
        list: Una lista de listas, donde cada lista contiene los resultados
        de la tabla de multiplicar para un número del 1 al 10.
    """
    tabla = []
    for numero in range(1, 11):
        resultados = []
        for multiplicador in range(1, 11):
            resultados.append(numero * multiplicador)
        tabla.append(resultados)
    return tabla


def mostrarTabla(tabla):
    """
    Muestra la tabla de multiplicar en la pantalla.

    Args:
        tabla (list): Una lista de listas que contiene las tablas de multiplicar.
    """
    for numero in range(len(tabla)):
        print("Tabla del:", numero + 1)
        for multiplicador in range(len(tabla[numero])):
            print(numero + 1, "x", multiplicador + 1, "=", tabla[numero][multiplicador])
        print()


def main():
    # Procesamiento
    tabla = calcularTablaMultiplicar()
    
    # Salida
    mostrarTabla(tabla)


if __name__ == '__main__':
    main()

