import pytest
from src.ejercicio2_2_18 import contarPares

def test_contarPares():
    # Prueba con una lista sin numeros pares
    assert contarPares([1, 3, 5, 7]) == 0

    # Prueba con una lista de solo numeros pares
    assert contarPares([2, 4, 6, 8]) == 4

    # Prueba con una lista de numeros mixtos
    assert contarPares([1, 2, 3, 4, 5]) == 2