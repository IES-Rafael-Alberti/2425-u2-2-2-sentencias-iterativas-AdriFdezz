[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qQgBV5uk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16653889&assignment_repo_type=AssignmentRepo)
# Práctica 2.2: Sentencias iterativas

Apoyate en los siguientes recursos para realizar la práctica:

[U2: 1. Sentencias iterativas](https://revilofe.github.io/section1/u02/practica/PROG-U2.-Practica002/)

---

# Título de la Actividad

## Identificación de la Actividad
- **ID de la Actividad:** Práctica 2.2: Sentencias iterativas y saltos
- **Módulo:** PROG
- **Unidad de Trabajo:** Unidad 2, Sentencias condicionales y repetitivas
- **Fecha de Creación:** 17/10/2024
- **Fecha de Entrega:** 23/10/2024
- **Alumno(s):** 
  - **Nombre y Apellidos:** Adrian Fernandez Garrido
  - **Correo electrónico:** afergar613@g.educaand.es
  - **Iniciales del Alumno/Grupo:** AFG

## Descripción de la Actividad
- Se realizan ejercicios sobre sentencias iterativas y sus respectivos test.

## Instrucciones de Compilación y Ejecución
1. **Requisitos Previos:**
   - Python, version: 3.11.9
   - IDE: Visual Studio Code

2. **Pasos para Compilar el Código:**

- No es necesario compilar es python.

3. **Pasos para Ejecutar el Código:**

- Se ejecuta desde el propio IDE

4. **Ejecución de Pruebas:**
   ```bash
   pytest [el nombre del test]
   ```

## Desarrollo de la Actividad
### Descripción del Desarrollo

- Se realiza los ejecicios respetando el SRP y documentando todas las funciones.
- Se separa entrada, procesamiento de salida en el main del ejercicio.
- Se hace uso de listas para facilitar los ejercicios.
- Se realizan los test y en varios casos se usa monkeypatch o capfd si fuera necesario         simular un input o capturar una salida.
- No se realizan mas ejercicios o test por falta de tiempo.

### Código Fuente

- [Ejemplo ejercicio2_2_9](src/ejercicio2_2_9.py)

 ```python
   """
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

def verificarContrasena(contrasenaAlmacenada: str) -> bool:
    """
    Pide al usuario que ingrese la contraseña hasta que la introduzca correctamente.
    
    Si el usuario ingresa una cadena vacia, muestra un mensaje de error.

    Args:
        contrasenaAlmacenada (str): La contraseña correcta que debe ser ingresada.

    Returns:
        bool: Devuelve True cuando se introduce la contraseña correcta.
    """
    contrasenaIngresada = ""

    while contrasenaIngresada != contrasenaAlmacenada:
        contrasenaIngresada = input("Introduce la contraseña: ")

        if contrasenaIngresada.strip() == "":
            print("Error: La contraseña no puede estar vacia.")
        elif contrasenaIngresada != contrasenaAlmacenada:
            print("Contraseña incorrecta, intentalo de nuevo.")

    return True

def mostrarMensajeBienvenida():
    """hol
    Muestra un mensaje de bienvenida cuando se introduce la contraseña correcta.
    """
    print("Contraseña correcta.")

def main():
    # Entrada
    contrasenaAlmacenada = "hola123"

    # Procesamiento
    contrasenaCorrecta = verificarContrasena(contrasenaAlmacenada)

    # Salida
    if contrasenaCorrecta:
        mostrarMensajeBienvenida()

if __name__ == '__main__':
    main()

   ```

### Ejemplos de Ejecución
- **Entrada y salida 1:** Entrada con una contraseña incorrecta y vuelve a pedirla

  ```bash
   Introduce la contraseña: hola
   Contraseña incorrecta, intentalo de nuevo.
   Introduce la contraseña:
   ```

- **Entrada y salida 2:** Entrada con la contraseña correcta

   ```bash
   Introduce la contraseña: hola123
   Contraseña correcta.
   ```

### Resultados de Pruebas

- [Ejemplo test_ejercicio9](tests/test_ejercicio9.py)

 ```python
   import pytest
   from src.ejercicio2_2_9 import verificarContrasena

   def test_verificarContrasena(monkeypatch):
       # Probar una entrada mala y otra buena
       inputs = iter(['malapass', 'hola123'])
       monkeypatch.setattr('builtins.input', lambda _: next(inputs))

       assert verificarContrasena('hola123') == True
   ```

- Se realiza un test sobre la funcion verificar contraseña con monkeypatch para simular el input.

## Conclusiones

- Tras la realizacion de este ejercicio hemos aprendido a utilizar mejor las sentencias iterativas y el uso de listas tambien hemos realizado test utilizando monkeypatch y capfd de esta forma podemos hacer las pruebas de una forma mas completa no se han relizado mas ejericios por falta de tiempo debido a que toman mas tiempo para hacerse de lo que parece.

## Referencias y Fuentes

[Revilofe](https://revilofe.github.io/section1/)

### Notas Adicionales:
1. **Nombres de Archivos y Repositorios:**
   - Asegúrate de que el nombre del archivo o repositorio siga la estructura definida: `XXX-idActividad-Iniciales`.
2. **Permisos:**
   - Verifica que el profesor tenga los permisos necesarios para acceder al repositorio o documento.
3. **Formato:**
   - Si se entrega en formato PDF o Google Docs, asegúrate de cumplir con el mínimo y máximo de folios establecidos.
4. **Compilación y Ejecución:**
   - Detalla claramente cómo compilar y ejecutar el código, incluyendo las instrucciones en el archivo `README.md`.
