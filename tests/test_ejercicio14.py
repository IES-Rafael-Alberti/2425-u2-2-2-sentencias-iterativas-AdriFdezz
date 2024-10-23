import pytest
from src.ejercicio2_2_14 import procesarNumeros

def test_procesarNumeros():
    # Prueba de suma normal
    assert procesarNumeros([1, 2, 3]) == 6
    
    # Prueba de suma con numeros negativos
    assert procesarNumeros([-1, -2, -3]) == -6
