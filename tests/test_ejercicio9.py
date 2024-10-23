import pytest
from src.ejercicio2_2_9 import verificarContrasena

def test_verificarContrasena(monkeypatch):
    # Probar una entrada mala y otra buena
    inputs = iter(['malapass', 'hola123'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert verificarContrasena('hola123') == True
