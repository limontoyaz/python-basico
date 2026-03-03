"""
test_operaciones.py
===================
Tests para las operaciones aritméticas básicas.

¿Cómo ejecutar estos tests?
    En la terminal (dentro de la carpeta del proyecto):
        pytest tests/
    o con más detalle:
        pytest tests/ -v

Conceptos de pytest que verás aquí:
- assert          → verificar que algo sea verdadero
- pytest.raises   → verificar que se lance una excepción
- parametrize     → ejecutar el mismo test con distintos datos
- fixtures        → datos reutilizables entre tests
"""

import pytest
from src.calculadora import sumar, restar, multiplicar, dividir, potencia, es_par


# ─────────────────────────────────────────
# TESTS SIMPLES (el patrón más básico)
# ─────────────────────────────────────────

class TestSumar:
    """Agrupa todos los tests de la función sumar()."""

    #def test_suma_positivos(self):
        """Suma dos números positivos."""
        #resultado =
        #assert 

    def test_suma_con_cero(self):
        """Sumar cero no cambia el valor."""
        assert sumar(5, 0) == 5
        assert sumar(0, 5) == 5

    def test_suma_negativos(self):
        """Sumar dos negativos da un negativo."""
        assert sumar(-2, -3) == -5

    def test_suma_flotantes(self):
        """Suma con decimales; usamos pytest.approx para comparar floats."""
        # No hagas: assert 0.1 + 0.2 == 0.3  → ¡falla por precisión!
        assert sumar(0.1, 0.2) == pytest.approx(0.3)


class TestRestar:
    def test_resta_basica(self):
        assert restar(10, 3) == 7

    def test_resta_resultado_negativo(self):
        assert restar(3, 10) == -7

    def test_resta_mismos_numeros(self):
        assert restar(5, 5) == 0


class TestMultiplicar:
    def test_multiplicar_positivos(self):
        assert multiplicar(4, 5) == 20

    def test_multiplicar_por_cero(self):
        assert multiplicar(99, 0) == 0

    def test_multiplicar_negativos(self):
        """Negativo × negativo = positivo."""
        assert multiplicar(-3, -4) == 12

    def test_multiplicar_mixtos(self):
        """Positivo × negativo = negativo."""
        assert multiplicar(5, -2) == -10


# ─────────────────────────────────────────
# TESTS DE EXCEPCIONES
# ─────────────────────────────────────────

class TestDividir:
    def test_division_normal(self):
        assert dividir(10, 2) == 5.0

    def test_division_decimal(self):
        assert dividir(7, 2) == pytest.approx(3.5)

    def test_division_entre_cero_lanza_excepcion(self):
        """pytest.raises verifica que se lance la excepción correcta."""
        with pytest.raises(ValueError):
            dividir(10, 0)

    def test_division_entre_cero_mensaje_correcto(self):
        """También podemos verificar el mensaje del error."""
        with pytest.raises(ValueError, match="No se puede dividir entre cero"):
            dividir(5, 0)


# ─────────────────────────────────────────
# TESTS PARAMETRIZADOS (misma lógica, distintos datos)
# ─────────────────────────────────────────




#def test_potencia_parametrizada():
    """
    pytest ejecuta este test UNA VEZ por cada fila de la tabla de arriba.
    Así evitamos copiar/pegar el mismo test 5 veces.
    """
    #assert potencia(base, exp) == esperado


@pytest.mark.parametrize("numero, es_par_esperado", [
    (0,  True),
    (1,  False),
    (2,  True),
    (7,  False),
    (100, True),
    (-4, True),
    (-3, False),
])
def test_es_par_parametrizado(numero, es_par_esperado):
    """Verifica es_par() con varios casos de borde."""
    assert es_par(numero) == es_par_esperado
