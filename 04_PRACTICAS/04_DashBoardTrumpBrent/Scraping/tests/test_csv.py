import sys
import os
import csv

# Añadir src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_csv_structure():
    print("🧪 Probando estructura y columnas del CSV...")
    
    csv_path = "data/raw/truths_export.csv"
    if not os.path.exists(csv_path):
        print(f"⚠️ No se encontró el archivo {csv_path}. Ejecuta primero el scraper.")
        return

    expected_columns = ["ID", "Time", "Tweet URL", "Tweet Text"]
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        
        print(f"Columnas detectadas: {header}")
        
        # Validar nombres de columnas
        assert header == expected_columns, f"❌ Las columnas no coinciden. Esperado: {expected_columns}"
        print("✅ Columnas validadas correctamente.")
        
        # Validar contenido mínimo
        first_row = next(reader, None)
        if first_row:
            print(f"✅ Ejemplo de datos: {first_row}")
            # El ID debe empezar con @ o ser 'null'
            assert first_row[0].startswith("@") or first_row[0] == "null"
            # La URL debe ser absoluta si existe
            assert first_row[2].startswith("https://") or first_row[2] == "null"
        else:
            print("⚠️ El archivo está vacío (solo cabeceras).")

if __name__ == "__main__":
    test_csv_structure()
