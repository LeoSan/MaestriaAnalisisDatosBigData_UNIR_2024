import asyncio
import argparse
import csv
import os
from playwright.async_api import async_playwright
from engine import get_browser_context, handle_popups, scroll_and_capture
from parser import TruthSocialScraper

async def run_scraper():
    # Configuración de argumentos desde terminal
    parser = argparse.ArgumentParser(description="Scraper Robusto de Truth Social (Trump 2026)")
    parser.add_argument("--limit", type=int, default=None, help="Límite opcional de posts")
    parser.add_argument("--year", type=int, default=2026, help="Año objetivo de extracción")
    parser.add_argument("--batch-size", type=int, default=50, help="Registros por bloque para escritura")
    parser.add_argument("--output", type=str, default="data/raw/trump_2026_truths.csv", help="Ruta de salida")
    args = parser.parse_args()

    # Asegurar que el directorio de datos existe
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    fieldnames = ["ID", "Time", "Year", "Tweet URL", "Tweet Text"]
    
    # Función para guardar bloques de 50 registros
    def save_to_csv(data_batch):
        file_exists = os.path.isfile(args.output)
        with open(args.output, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            for row in data_batch:
                cleaned_row = {field: (row.get(field) or "null") for field in fieldnames}
                writer.writerow(cleaned_row)

    async with async_playwright() as p:
        browser, context = await get_browser_context(p, headless=True)
        page = await context.new_page()
        
        url = "https://truthsocial.com/@realDonaldTrump"
        print(f"🌐 Iniciando sesión en: {url}")
        
        try:
            # Navegación inicial
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(8)
            await handle_popups(page)
            await asyncio.sleep(2)
            
            # Verificación de estructura base
            await page.wait_for_selector('div[data-testid="virtuoso-item-list"]', timeout=60000)
            print("✅ Estructura base cargada.")
            
            # Instanciamos el scraper
            ts_parser = TruthSocialScraper()
            
            # Callback para que el motor use el parser
            def parse_html(html):
                ts_parser.results = [] # Limpiar para cada frame
                ts_parser.extract_data(html)
                return ts_parser.results

            # Ejecutar recolección robusta
            await scroll_and_capture(
                page, 
                limit=args.limit, 
                target_year=args.year, 
                batch_size=args.batch_size,
                parser_callback=parse_html,
                save_callback=save_to_csv
            )
            
            print(f"🎊 ¡Proceso completado! Datos en: {args.output}")

        except Exception as e:
            print(f"❌ Fallo crítico: {e}")
            await page.screenshot(path="data/raw/last_recovery_error.png")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(run_scraper())
