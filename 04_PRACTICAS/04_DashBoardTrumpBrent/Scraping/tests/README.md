# Pruebas Unitarias y de Estructura

En este directorio se encuentran los scripts utilizados para validar los componentes del scraper de forma aislada.

## 🧪 Tests Disponibles

1.  **Validación de Fechas**: 
    Prueba la lógica de transformación de fechas de Truth Social al formato ISO.
    ```bash
    python3 -m uv run tests/test_utils.py
    ```

2.  **Validación de Estructura HTML**:
    Comprueba si los selectores de BeautifulSoup siguen siendo válidos contra una muestra local.
    ```bash
    python3 -m uv run tests/test_parser.py
    ```

3.  **Validación de Formato CSV**:
    Verifica que las columnas sean exactamente `ID, Time, Tweet URL, Tweet Text`.
    ```bash
    python3 -m uv run tests/test_csv.py
    ```

