import pytest
from src.ejercicio2_2_4 import cuentaAtras

def test_cuentaAtras():
    # Probar con el numero 5
    assert cuentaAtras(5) == [5, 4, 3, 2, 1, 0]
    
    # Probar con 1 solo numero
    assert cuentaAtras(1) == [1, 0]
    
    # Probar con el numero 0
    assert cuentaAtras(0) == [0]
    
    # Probar con un numero negativo
    assert cuentaAtras(-5) == []