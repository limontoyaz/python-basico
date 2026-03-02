# Hace que la carpeta src sea un paquete Python.
from .calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    es_par,
    maximo,
    promedio,
    saludar,
    contar_vocales,
    invertir_texto,
)

__all__ = [
    "sumar", "restar", "multiplicar", "dividir",
    "potencia", "es_par", "maximo", "promedio",
    "saludar", "contar_vocales", "invertir_texto",
]
