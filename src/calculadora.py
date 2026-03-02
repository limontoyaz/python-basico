"""
calculadora.py
==============
Módulo principal del proyecto Python Básico.

Aquí aprenderás sobre:
- Funciones
- Tipos de datos (int, float, str)
- Condicionales (if/elif/else)
- Manejo de excepciones (try/except)
- Docstrings
"""


# ─────────────────────────────────────────
# OPERACIONES BÁSICAS
# ─────────────────────────────────────────

def sumar(a: float, b: float) -> float:
    """Retorna la suma de dos números.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        La suma de a y b.

    Ejemplo:
        >>> sumar(3, 4)
        7
    """
    return a + b


def restar(a: float, b: float) -> float:
    """Retorna la resta de dos números (a - b).

    Ejemplo:
        >>> restar(10, 3)
        7
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna el producto de dos números.

    Ejemplo:
        >>> multiplicar(4, 5)
        20
    """
    return a * b


def dividir(a: float, b: float) -> float:
    """Retorna la división de a entre b.

    Lanza:
        ValueError: Si b es cero (no se puede dividir entre cero).

    Ejemplo:
        >>> dividir(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


# ─────────────────────────────────────────
# OPERACIONES AVANZADAS
# ─────────────────────────────────────────

def potencia(base: float, exponente: int) -> float:
    """Retorna base elevada al exponente.

    Ejemplo:
        >>> potencia(2, 8)
        256
    """
    return base ** exponente


def es_par(numero: int) -> bool:
    """Retorna True si el número es par, False si es impar.

    Ejemplo:
        >>> es_par(4)
        True
        >>> es_par(7)
        False
    """
    return numero % 2 == 0


def maximo(lista: list) -> float:
    """Retorna el valor máximo de una lista de números.

    Args:
        lista: Lista con al menos un elemento numérico.

    Lanza:
        ValueError: Si la lista está vacía.

    Ejemplo:
        >>> maximo([3, 7, 1, 9, 2])
        9
    """
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return max(lista)


def promedio(lista: list) -> float:
    """Retorna el promedio (media aritmética) de una lista de números.

    Lanza:
        ValueError: Si la lista está vacía.

    Ejemplo:
        >>> promedio([1, 2, 3, 4, 5])
        3.0
    """
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return sum(lista) / len(lista)


# ─────────────────────────────────────────
# TRABAJO CON STRINGS
# ─────────────────────────────────────────

def saludar(nombre: str) -> str:
    """Genera un saludo personalizado.

    Ejemplo:
        >>> saludar("María")
        '¡Hola, María! Bienvenida a Python 🐍'
    """
    return f"¡Hola, {nombre}! Bienvenida a Python 🐍"


def contar_vocales(texto: str) -> int:
    """Cuenta cuántas vocales (a,e,i,o,u) tiene un texto.

    La búsqueda no distingue mayúsculas de minúsculas.

    Ejemplo:
        >>> contar_vocales("Hola Mundo")
        4
    """
    vocales = "aeiouáéíóú"
    return sum(1 for letra in texto.lower() if letra in vocales)


def invertir_texto(texto: str) -> str:
    """Retorna el texto invertido.

    Ejemplo:
        >>> invertir_texto("Python")
        'nohtyP'
    """
    return texto[::-1]


# ─────────────────────────────────────────
# PUNTO DE ENTRADA (ejecutar directamente)
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 45)
    print("   🐍  Calculadora Python Básico  🐍")
    print("=" * 45)

    # Operaciones aritméticas
    print(f"\n  3  +  4  =  {sumar(3, 4)}")
    print(f"  10 -  3  =  {restar(10, 3)}")
    print(f"  6  x  7  =  {multiplicar(6, 7)}")
    print(f"  15 /  4  =  {dividir(15, 4)}")
    print(f"  2  ^ 10  =  {potencia(2, 10)}")

    # Listas
    numeros = [5, 3, 8, 1, 9, 2, 7]
    print(f"\n  Lista     : {numeros}")
    print(f"  Máximo    : {maximo(numeros)}")
    print(f"  Promedio  : {promedio(numeros):.2f}")

    # Strings
    print(f"\n  {saludar('Estudiante')}")
    print(f"  Vocales en 'Programación': {contar_vocales('Programación')}")
    print(f"  'Python' invertido       : {invertir_texto('Python')}")

    # División entre cero (manejo de error)
    print("\n  Intentando dividir entre 0...")
    try:
        dividir(5, 0)
    except ValueError as e:
        print(f"  ❌ Error capturado: {e}")

    print("\n  ✅ ¡Programa ejecutado con éxito!")
    print("=" * 45)
