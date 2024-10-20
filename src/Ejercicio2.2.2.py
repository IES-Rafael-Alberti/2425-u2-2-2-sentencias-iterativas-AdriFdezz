"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad).
"""

def leerEdad() -> int:
    """
    Lee la edad del usuario.
    Si la edad no es un numero valido o es menor o igual a cero, mostrara un mensaje de error y volvera a pedir la edad.
    :return: La edad introducida por el usuario.
    """

    edadValida = False
    edad = 0

    while not edadValida:
        try:
            entrada = input("Introduce tu edad: ")
            if entrada.strip() == "":
                raise ValueError("Error: La entrada no puede estar vacia.")
            edad = int(entrada)
            if edad <= 0:
                raise ValueError("Error: La edad debe ser un numero positivo.")
            edadValida = True
        except ValueError as errorMensaje:
            print(errorMensaje)
            
    return edad

def aniosCumplidos(edad: int) -> list:
    """
    Procesa y retorna todos los años que el usuario ha cumplido desde 1 hasta su edad.
    :param edad: La edad del usuario.
    :return: Una lista de años cumplidos.
    """

    todosLosAnios = []
    for anio in range(1, edad + 1):
        todosLosAnios.append(anio)

    return todosLosAnios

def mostrarResultado(anios: list):
    """
    Muestra por pantalla todos los años cumplidos.
    :param anios: Lista de años cumplidos.
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