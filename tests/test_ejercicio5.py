import pytest
from src.ejercicio2_2_5 import calcularInversion

def test_calcularInversion():
    # Inversion de 1000 con un interes del 10% durante 3 años
    assert calcularInversion(1000, 10, 3) == [1100.0, 1210.0, 1331.0]

    # Inversion de 1500 con un interes del 3% durante 3 años
    assert calcularInversion(1500, 3, 3) == [1545.0, 1591.35, 1639.09]
    
    # Inversion de 2000 con un interes del 0% durante 3 años
    assert calcularInversion(2000, 0, 3) == [2000.0, 2000.0, 2000.0]