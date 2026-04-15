import asyncio
import re
from playwright.async_api import async_playwright

async def get_browser_context(p, headless=True):
    """Lanza el navegador y configura el contexto."""
    browser = await p.chromium.launch(headless=headless)
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    return browser, context

async def handle_popups(page):
    """Maneja cookies y anuncios detectados."""
    # 1. Cookies
    try:
        cookie_btn = page.get_by_role("button", name=re.compile(r"Accept all|ACEPTAR|OK", re.I))
        if await cookie_btn.is_visible(timeout=2000):
            await cookie_btn.click()
            print("✅ Cookies aceptadas.")
    except: pass

    # 2. Anuncios y Modales (Featured Ad)
    # Buscamos botones de cierre comunes: "X", "Close", "Cerrar"
    try:
        # Intentar por título, aria-label o texto de cierre común
        selectors = [
            'button[title="Close"]',
            'button[aria-label="Close"]',
            'button:has-text("X")',
            'div[role="button"]:has-text("X")'
        ]
        for sel in selectors:
            btn = page.locator(sel).first
            if await btn.is_visible(timeout=2000):
                await btn.click()
                print(f"✅ Modal/Pop-up cerrado con selector: {sel}")
                await asyncio.sleep(1)
    except: pass
    
    # Intento desesperado: múltiples Escapes
    for _ in range(3):
        await page.keyboard.press("Escape")
        await asyncio.sleep(0.5)


async def scroll_and_capture(page, limit=None, target_year=None, batch_size=50, parser_callback=None, save_callback=None):
    """
    Algoritmo de scroll robusto con filtrado por año y guardado incremental.
    """
    unique_results = []
    seen_urls = set()
    buffer = []
    consecutive_no_new = 0
    total_captured = 0
    
    print(f"📥 Iniciando recolección (Año: {target_year or 'Cualquiera'}, Bloque: {batch_size}, Límite: {limit or '∞'})...")
    
    while True:
        # Extraer posts visibles actualmente
        html = await page.content()
        new_items = parser_callback(html)
        
        found_now = 0
        stop_by_year = False
        
        for item in new_items:
            # Usar URL del post para deduplicación (más preciso que el texto)
            post_url = item.get('Tweet URL')
            post_year = item.get('Year')

            # Si el post es de un año anterior al solicitado, paramos el proceso total
            if target_year and post_year and post_year < target_year:
                print(f"🛑 Detectado post de {post_year}. Finalizando recolección de {target_year}.")
                stop_by_year = True
                break

            # Si el post es del año correcto (o no hay filtro)
            if (not target_year or post_year == target_year) and post_url not in seen_urls:
                unique_results.append(item)
                buffer.append(item)
                seen_urls.add(post_url)
                found_now += 1
                total_captured += 1

        if stop_by_year:
            break

        # Manejo de persistencia en bloques
        if len(buffer) >= batch_size:
            if save_callback:
                print(f"💾 Guardando bloque de {len(buffer)} registros...")
                save_callback(buffer)
                buffer = []

        if found_now == 0:
            consecutive_no_new += 1
        else:
            consecutive_no_new = 0
            print(f"📊 Capturados en sesión: {total_captured} (Total único: {len(unique_results)})")

        # Límites por cantidad si se solicita
        if limit and len(unique_results) >= limit:
            print(f"✅ Se alcanzó el límite solicitado: {limit}")
            break

        if consecutive_no_new > 20:
            print("🏁 Se alcanzó el final del feed o el contenido no carga.")
            break
            
        # Scroll y espera dinámica
        await page.mouse.wheel(0, 2000)
        await asyncio.sleep(2.5) # Un poco más lento para evitar bloqueos
        
    # Guardar residuo del buffer
    if buffer and save_callback:
        save_callback(buffer)
        
    return unique_results
