import sys
import os

# Añadir src al path para poder importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from parser import TruthSocialScraper

def test_html_parsing():
    print("🧪 Probando parser contra HTML de referencia...")
    
    # Intentar cargar el archivo de estructura local
    html_path = "data/structure/estructura.html"
    if not os.path.exists(html_path):
        print(f"⚠️ No se encontró {html_path}, abortando test.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    scraper = TruthSocialScraper(limit=5)
    success = scraper.extract_data(html_content)
    
    if success and len(scraper.results) > 0:
        print(f"✅ ÉXITO: Se extrajeron {len(scraper.results)} posts del HTML local.")
        for r in scraper.results:
            print(f"- [{r['fecha']}] {r['mensaje'][:50]}...")
    else:
        print("❌ FALLO: No se pudieron extraer datos del HTML de referencia.")

if __name__ == "__main__":
    test_html_parsing()
