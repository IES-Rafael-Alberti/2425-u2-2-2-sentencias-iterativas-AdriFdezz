import pytest
from src.ejercicio2_2_2 import aniosCumplidos

def test_aniosCumplidos():
    # Probar con una edad de 5 años
    assert aniosCumplidos(5) == [1, 2, 3, 4, 5]
    
    # Probar con una edad de 1 año
    assert aniosCumplidos(1) == [1]
    
    # Probar con una edad de 0 años
    assert aniosCumplidos(0) == []

    # Probar con una edad negativa
    assert aniosCumplidos(-5) == []