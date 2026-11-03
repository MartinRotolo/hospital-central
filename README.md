# Hospital Central - Módulo de facturación

## Instalación

```
pip install -r requirements-dev.txt
git config core.hooksPath hooks
```

El segundo comando activa el pre-commit hook de la carpeta `hooks`, que ejecuta
el formatter (black), el linter (ruff) y las pruebas unitarias con cobertura
(pytest) antes de cada commit.

## Ejecutar las pruebas

```
python -m pytest --cov --cov-report=term-missing
```
