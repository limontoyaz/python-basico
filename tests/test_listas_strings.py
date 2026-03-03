"""
test_listas_strings.py
======================
Tests para funciones que trabajan con listas y strings.

Nuevos conceptos de pytest que verás aquí:
- Fixtures          → datos compartidos entre tests
- conftest.py       → fixtures globales (ver ../conftest.py)
"""

import pytest
from src.calculadora import maximo, promedio, saludar, contar_vocales, invertir_texto


# ─────────────────────────────────────────
# FIXTURE LOCAL (disponible solo en este archivo)
# ─────────────────────────────────────────


#def lista_numeros():
    """
    Un fixture es una función que prepara datos para los tests.
    pytest la ejecuta automáticamente cuando un test la pide como parámetro.
    """
    



#def lista_con_negativos():
    


# ─────────────────────────────────────────
# TESTS DE LISTAS
# ─────────────────────────────────────────

class TestMaximo:
    #Función para crequear maximo lista

    def test_maximo_lista_negativos(self, lista_con_negativos):
        assert maximo(lista_con_negativos) == -1

    def test_maximo_un_elemento(self):
        assert maximo([42]) == 42

    def test_maximo_con_repetidos(self):
        assert maximo([3, 3, 3]) == 3

    def test_maximo_lista_vacia_lanza_error(self):
        with pytest.raises(ValueError):
            maximo([])


class TestPromedio:
    def test_promedio_basico(self, lista_numeros):
        # [5,3,8,1,9,2,7] → suma=35, len=7, promedio=5.0
        assert promedio(lista_numeros) == pytest.approx(5.0)

    def test_promedio_un_elemento(self):
        assert promedio([10]) == 10.0

    def test_promedio_lista_vacia_lanza_error(self):
        with pytest.raises(ValueError, match="vacía"):
            promedio([])

    def test_promedio_negativos(self):
        assert promedio([-2, 0, 2]) == pytest.approx(0.0)

    def test_promedio_flotantes(self):
        assert promedio([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=1e-3)


# ─────────────────────────────────────────
# TESTS DE STRINGS
# ─────────────────────────────────────────

class TestSaludar:
    def test_saludo_contiene_nombre(self):
        resultado = saludar("Ana")
        assert "Ana" in resultado

    def test_saludo_contiene_hola(self):
        resultado = saludar("Carlos")
        assert "Hola" in resultado or "hola" in resultado

    def test_saludo_es_string(self):
        """Verificar el tipo de dato retornado."""
        assert isinstance(saludar("Pedro"), str)


class TestContarVocales:
    def test_vocales_palabra_simple(self):
        assert contar_vocales("hola") == 2     # o, a

    def test_vocales_sin_vocales(self):
        assert contar_vocales("rhythm") == 0

    def test_vocales_ignora_mayusculas(self):
        """La función debe tratar A igual que a."""
        assert contar_vocales("AEIOU") == 5
        assert contar_vocales("aeiou") == 5

    def test_vocales_string_vacio(self):
        assert contar_vocales("") == 0

    def test_vocales_con_tildes(self):
        """Las vocales con tilde también cuentan."""
        assert contar_vocales("Programación") == 5  # o, a, a, i, ó

#### Test parametrizados


    
    def test_vocales_parametrizado(self, texto, esperado):
        assert contar_vocales(texto) == esperado


class TestInvertirTexto:
    def test_invertir_palabra(self):
        assert invertir_texto("Python") == "nohtyP"

    def test_invertir_palindromo(self):
        """Un palíndromo invertido es igual a sí mismo."""
        assert invertir_texto("anilina") == "anilina"

    def test_invertir_string_vacio(self):
        assert invertir_texto("") == ""

    def test_invertir_un_caracter(self):
        assert invertir_texto("x") == "x"

    def test_invertir_con_espacios(self):
        assert invertir_texto("hola mundo") == "odnum aloh"

    def test_doble_inversion_devuelve_original(self):
        """Invertir dos veces debe dar el texto original."""
        original = "¡Aprendiendo pytest!"
        assert invertir_texto(invertir_texto(original)) == original
