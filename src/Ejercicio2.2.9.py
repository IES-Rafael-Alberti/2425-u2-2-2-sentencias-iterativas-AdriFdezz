"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

def verificarContrasena(contrasenaAlmacenada: str) -> bool:
    """
    Pide al usuario que ingrese la contraseña hasta que la introduzca correctamente.
    
    Si el usuario ingresa una cadena vacia, muestra un mensaje de error.

    Args:
        contrasenaAlmacenada (str): La contraseña correcta que debe ser ingresada.

    Returns:
        bool: Devuelve True cuando se introduce la contraseña correcta.
    """
    contrasenaIngresada = ""

    while contrasenaIngresada != contrasenaAlmacenada:
        contrasenaIngresada = input("Introduce la contraseña: ")

        if contrasenaIngresada.strip() == "":
            print("Error: La contraseña no puede estar vacia.")
        elif contrasenaIngresada != contrasenaAlmacenada:
            print("Contraseña incorrecta, intentalo de nuevo.")

    return True

def mostrarMensajeBienvenida():
    """hol
    Muestra un mensaje de bienvenida cuando se introduce la contraseña correcta.
    """
    print("Contraseña correcta.")

def main():
    # Entrada
    contrasenaAlmacenada = "hola123"

    # Procesamiento
    contrasenaCorrecta = verificarContrasena(contrasenaAlmacenada)

    # Salida
    if contrasenaCorrecta:
        mostrarMensajeBienvenida()

if __name__ == '__main__':
    main()
