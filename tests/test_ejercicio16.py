import pytest
from src.ejercicio2_2_16 import encontrarMayor

def test_encontrarMayor():
    # Prueba con varios numeros positivos
    assert encontrarMayor([10, 20, 30, 5, 15]) == 30

    # Prueba con un solo numero
    assert encontrarMayor([50]) == 50

    # Prueba con numeros iguales
    assert encontrarMayor([2, 5, 5, 4]) == 5
