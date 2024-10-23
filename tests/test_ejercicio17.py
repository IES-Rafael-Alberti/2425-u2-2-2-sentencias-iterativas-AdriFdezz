import pytest
from src.ejercicio2_2_17 import sumarDigitos

def test_sumarDigitos():

    # Prueba con un numero de varios digitos
    assert sumarDigitos(1234) == 10
    
    # Prueba con el numero 10
    assert sumarDigitos(10) == 1