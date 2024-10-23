import pytest
from src.ejercicio2_2_12 import contarLetras

# Prueba para contar las letras
def test_contarLetras():
    assert contarLetras("hola mundo", "o") == 2