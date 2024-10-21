"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad).
"""

def leerEdad() -> int:
    """
    Lee la edad del usuario.

    Si la edad no es un numero valido o es menor o igual a cero, mostrara un mensaje de error y volvera a pedir la edad.

    Returns:
        int: La edad introducida por el usuario.
    """

    edadValida = False
    edad = 0

    while not edadValida:
        entrada = input("Introduce tu edad: ")
        try:
            if entrada.strip() == "":
                print("Error: La entrada no puede estar vacia.")
            else:
                edad = int(entrada)
                if edad <= 0:
                    print("Error: La edad debe ser un numero positivo.")
                else:
                    edadValida = True
        except ValueError:
            print("Error: Debes introducir un numero valido.")
            
    return edad

def aniosCumplidos(edad: int) -> list:
    """
    Procesa y retorna todos los años que el usuario ha cumplido desde 1 hasta su edad.

    Args:
        edad (int): La edad del usuario.

    Returns:
        list: Una lista de años cumplidos.
    """

    todosLosAnios = []
    for anio in range(1, edad + 1):
        todosLosAnios.append(anio)

    return todosLosAnios

def mostrarResultado(anios: list):
    """
    Muestra por pantalla todos los años cumplidos.

    Args:
        anios (list): Lista de años cumplidos.
    """

    for anio in anios:
        print(anio)

def main():
    #Entrada
    edad = leerEdad()

    #Procesamiento
    anios = aniosCumplidos(edad)

    #Salida
    mostrarResultado(anios)

if __name__ == '__main__':
    main()