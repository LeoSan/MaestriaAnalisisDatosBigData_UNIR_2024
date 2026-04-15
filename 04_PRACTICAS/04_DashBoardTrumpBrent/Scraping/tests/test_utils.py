import sys
import os

# Añadir src al path para poder importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import parse_truth_date, clean_text

def test_date_parsing():
    print("🧪 Probando parseo de fechas...")
    test_dates = [
        "Apr 06, 2026, 7:13 PM",
        "Jan 20, 2025, 12:00 PM",
        "Dec 31, 2026, 11:59 PM"
    ]
    for d in test_dates:
        result = parse_truth_date(d)
        print(f"Original: {d} -> Procesada: {result}")
        assert result is not None

def test_text_cleaning():
    print("\n🧪 Probando limpieza de texto...")
    raw_text = "   Este es un   mensaje  con muuchos   espacios.   \n\n"
    cleaned = clean_text(raw_text)
    print(f"Original: '{raw_text}'\nLimpio  : '{cleaned}'")
    assert "  " not in cleaned

if __name__ == "__main__":
    test_date_parsing()
    test_text_cleaning()
    print("\n✅ ¡Todas las pruebas de utilidades pasaron!")
