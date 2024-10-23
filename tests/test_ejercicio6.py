import pytest
from src.ejercicio2_2_6 import mostrarTriangulo

def test_mostrarTriangulo(capfd):
    # Triangulo de altura 5
    mostrarTriangulo(5)
    capturar = capfd.readouterr()
    assert capturar.out == "*\n**\n***\n****\n*****\n"