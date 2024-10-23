import pytest
from src.ejercicio2_2_8 import generarTriangulo, mostrarTriangulo

def test_mostrarTriangulo(capfd):
    # Probar con 5 alturas
    triangulo = generarTriangulo(5)
    mostrarTriangulo(triangulo)
    captured = capfd.readouterr()

    # Preparar la salida esperada
    salidaEsperada = ""
    for fila in triangulo:
        salidaEsperada += " ".join(str(num) for num in fila) + "\n"

    assert captured.out == salidaEsperada