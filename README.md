# Python Básico — Proyecto de Aprendizaje

Proyecto educativo para aprender los conceptos fundamentales de Python  
y familiarizarse con el flujo de trabajo profesional usando **VS Code** y **pytest**.

---

## Estructura del proyecto

```
python-basico/
│
├── src/
│   ├── __init__.py          ← convierte src en un paquete Python
│   └── calculadora.py       ← funciones que vamos a estudiar y testear
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py          ← fixtures compartidas entre todos los tests
│   ├── test_operaciones.py  ← tests de suma, resta, división, potencia…
│   └── test_listas_strings.py ← tests de listas y cadenas de texto
│
├── .vscode/
│   ├── settings.json        ← configuración de VS Code para el proyecto
│   └── extensions.json      ← extensiones recomendadas
│
├── .gitignore               ← archivos que Git debe ignorar
├── pytest.ini               ← configuración de pytest
├── requirements.txt         ← dependencias del proyecto
└── README.md                ← este archivo
```

---

## Configuración inicial (paso a paso)

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd python-basico
```

### 2. Crear un entorno virtual

> Un entorno virtual aísla las dependencias del proyecto.

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

Cuando el entorno esté activo verás `(.venv)` al inicio de tu terminal.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Abrir en VS Code

```bash
code .
```

> VS Code detectará el entorno virtual automáticamente.  
> Si te pide seleccionar un intérprete, elige el que dice `.venv`.

---

## Ejecutar el programa principal

```bash
python src/calculadora.py
```

Verás una demostración de todas las funciones del módulo.

---

## Ejecutar los tests con pytest

### Todos los tests
```bash
pytest
```

### Con detalle (verbose)
```bash
pytest -v
```

### Un archivo específico
```bash
pytest tests/test_operaciones.py -v
```

### Una clase o función específica
```bash
pytest tests/test_operaciones.py::TestSumar -v
pytest tests/test_operaciones.py::TestSumar::test_suma_positivos -v
```

### Con reporte de cobertura de código
```bash
pytest --cov=src --cov-report=term-missing
```

### Desde VS Code
1. Abre el panel **Testing** (ícono del matraz en la barra lateral).
2. Haz clic en ▶️ para ejecutar todos los tests.
3. Los tests pasan (✅) o fallan (❌) visualmente.

---

##  Conceptos de Python cubiertos

| Concepto | Dónde verlo |
|---|---|
| Funciones y parámetros | `src/calculadora.py` |
| Tipos: `int`, `float`, `str`, `bool`, `list` | Todo el proyecto |
| Condicionales `if/elif/else` | `dividir()`, `maximo()` |
| Manejo de errores `try/except` | `__main__` en `calculadora.py` |
| Excepciones `raise ValueError` | `dividir()`, `maximo()`, `promedio()` |
| f-strings | `saludar()`, `__main__` |
| Comprensión de listas | `contar_vocales()` |
| Slicing de strings | `invertir_texto()` |
| Módulos y paquetes | `src/__init__.py` |
| Type hints | Todos los parámetros y retornos |
| Docstrings | Todas las funciones |

---

##  Conceptos de pytest cubiertos

| Concepto | Dónde verlo |
|---|---|
| `assert` básico | Todos los tests |
| Clases de test (`class Test...`) | `test_operaciones.py` |
| `pytest.approx` para floats | `TestSumar`, `TestDividir` |
| `pytest.raises` para excepciones | `TestDividir`, `TestMaximo` |
| Tests parametrizados (`@pytest.mark.parametrize`) | `test_potencia_parametrizada`, `test_es_par_parametrizado` |
| Fixtures locales (`@pytest.fixture`) | `test_listas_strings.py` |
| Fixtures globales (`conftest.py`) | `tests/conftest.py` |
| `scope="session"` en fixtures | `conftest.py` |
| `@pytest.mark.skip` | `test_listas_strings.py` |
| `@pytest.mark.xfail` | `test_listas_strings.py` |
| Configuración (`pytest.ini`) | `pytest.ini` |

---

##  Ejercicios propuestos

Una vez que entiendas el código, intenta resolver estos ejercicios:

1. **Fácil** — Agrega una función `minimo(lista)` en `calculadora.py` y escribe sus tests.
2. **Fácil** — Agrega una función `es_impar(numero)` y testéala con `parametrize`.
3. **Medio** — Agrega `factorial(n)` que lance `ValueError` si `n < 0`.
4. **Medio** — Agrega `es_palindromo(texto)` y escribe al menos 5 tests.
5. **Difícil** — Agrega `ordenar(lista, ascendente=True)` y crea una fixture en `conftest.py` que la use.

---

##  Extensiones recomendadas para VS Code

Al abrir el proyecto, VS Code sugerirá instalar:

- **Python** — soporte completo del lenguaje
- **Pylance** — autocompletado inteligente
- **Black Formatter** — formateo automático al guardar
- **Pylint** — detección de errores antes de ejecutar
- **Python Test Adapter** — panel visual de tests

---

##  Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Documentación de pytest](https://docs.pytest.org/)
- [PEP 8 — Guía de estilo Python](https://peps.python.org/pep-0008/)
- [Python para todos (curso gratuito)](https://www.py4e.com/lessons)

---

*¡Mucho ánimo! Recuerda: el mejor código es el que entiendes y el que tiene tests.* 🚀
