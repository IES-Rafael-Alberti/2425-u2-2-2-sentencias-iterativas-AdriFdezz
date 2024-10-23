import pytest
from src.ejercicio2_2_13 import procesarEntrada

def test_procesarEntrada(capfd, monkeypatch):
    # Probamos la entrada hasta introducir salir
    inputs = iter(['Hola', 'Mundo', 'salir'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    procesarEntrada()
    capturar = capfd.readouterr()
    
    assert capturar.out == 'Hola\nMundo\n'