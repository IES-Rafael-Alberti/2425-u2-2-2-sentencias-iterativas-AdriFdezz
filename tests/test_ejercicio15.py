import pytest
from src.ejercicio2_2_15 import procesarNumeros

def test_procesarNumeros():
    # Prueba con una lista de numeros positivos
    assert procesarNumeros([1, 2, 3]) == 6
    
    # Prueba con numeros repetidos
    assert procesarNumeros([2, 2, 2]) == 6
    
    # Prueba con una lista que contiene solo ceros
    assert procesarNumeros([0, 0, 0]) == 0
