import pytest
from src.ejercicio2_2_1 import repetirPalabra

def test_repetirPalabra():
    # Probar con una palabra normal
    assert repetirPalabra("hola") == "hola hola hola hola hola hola hola hola hola hola "
    
    # Probar con una palabra con numeros
    assert repetirPalabra("hola123") == "hola123 hola123 hola123 hola123 hola123 hola123 hola123 hola123 hola123 hola123 "
    
    # Probar con una palabra con caracteres especiales
    assert repetirPalabra("hol@") == "hol@ hol@ hol@ hol@ hol@ hol@ hol@ hol@ hol@ hol@ "