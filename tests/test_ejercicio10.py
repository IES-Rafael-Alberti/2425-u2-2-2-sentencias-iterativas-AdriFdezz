import pytest
from src.ejercicio2_2_10 import esPrimo

def test_esPrimo():
    # Prueba para numero primo
    assert esPrimo(2) == True
    
    # Prueba para numero no primo
    assert esPrimo(4) == False