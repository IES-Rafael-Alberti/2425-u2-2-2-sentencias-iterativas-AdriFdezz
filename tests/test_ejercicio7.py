import pytest
from src.ejercicio2_2_7 import calcularTablaMultiplicar, mostrarTabla

def test_calcularTablaMultiplicar(capfd):
    # Probar las tablas del 1 al 10
    tabla = calcularTablaMultiplicar()
    mostrarTabla(tabla)
    capturar = capfd.readouterr()

    # Preparar la salida esperada para no mostrar una cadena de texto gigante
    salidaEsperada = ""
    for numero in range(1, 11):
        salidaEsperada += "Tabla del: " + str(numero) + "\n"
        for multiplicador in range(1, 11):
            salidaEsperada += str(numero) + " x " + str(multiplicador) + " = " + str(numero * multiplicador) + "\n"
        salidaEsperada += "\n"

    assert capturar.out == salidaEsperada