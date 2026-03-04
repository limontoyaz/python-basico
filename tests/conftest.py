"""
conftest.py
===========
Archivo especial de pytest: las fixtures definidas aquí están disponibles
en TODOS los archivos de test del proyecto, sin necesidad de importarlas.

pytest lo detecta automáticamente al ejecutar los tests.
"""

import pytest


@pytest.fixture(scope="session")
def numeros_pequenios():
    """
    scope="session" → pytest crea esta fixture UNA SOLA VEZ
    para toda la sesión de tests (más eficiente que recrearla cada vez).
    """
    return [1, 2, 3, 4, 5]


@pytest.fixture
def numeros_grandes():
    """Sin scope → se recrea antes de cada test (comportamiento por defecto)."""
    return [100, 200, 300, 400, 500]


@pytest.fixture
def nombres_ejemplo():
    """Lista de nombres para tests de strings."""
    return ["Ana", "Luis", "María", "Carlos", "Sofía"]
