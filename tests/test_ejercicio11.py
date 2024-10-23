import pytest
from src.ejercicio2_2_11 import procesarPalabra

def test_procesarPalabra():
    # Prueba con palabras normales
    assert procesarPalabra("hola") == ['a', 'l', 'o', 'h']
    
    # Prueba con caracter especial
    assert procesarPalabra("Hol@") == ['@', 'l', 'o', 'H']

    # Prueba con una palabra con letras en mayusculas y minusculas
    assert procesarPalabra("AbCdEf") == ['f', 'E', 'd', 'C', 'b', 'A']

    # Test con palabras con espacios
    assert procesarPalabra("hola hola") == ['a', 'l', 'o', 'h', ' ', 'a', 'l', 'o', 'h']
