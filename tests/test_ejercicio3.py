import pytest
from src.ejercicio2_2_3 import numerosImpares

def test_numerosImpares():
    # Probar con el numero 5
    assert numerosImpares(5) == [1, 3, 5]
    
    # Probar con solo 1 numero
    assert numerosImpares(1) == [1]
    
    # Probar con un numero par
    assert numerosImpares(8) == [1, 3, 5, 7]
    
    # Probar con el numero 0
    assert numerosImpares(0) == []
    
    # Probar con un numero negativo
    assert numerosImpares(-5) == []