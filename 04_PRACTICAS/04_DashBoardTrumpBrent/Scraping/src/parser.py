import os
import json
import time
import re
from bs4 import BeautifulSoup
from utils import clean_text, parse_truth_date

class TruthSocialScraper:
    def __init__(self, limit=10):
        self.limit = limit
        self.base_url = "https://truthsocial.com/@realDonaldTrump"
        self.results = []
        # Selectores identificados
        self.SELECTORS = {
            "root": "virtuoso-item-list",
            "status": "status",
            "content": "status-content",
        }


    def validate_structure(self, soup):
        """
        Verifica si la estructura base existe. 
        Si no, aborta para evitar extracciones erróneas.
        """
        print("🔍 Validando estructura HTML...")
        root = soup.find("div", {"data-testid": self.SELECTORS["root"]})
        if not root:
            return False, "Eje principal (virtuoso-item-list) no encontrado."
        
        example_status = soup.find("div", {"data-testid": self.SELECTORS["status"]})
        if not example_status:
            return False, "Elemento de post (status) no encontrado."
            
        return True, "Estructura validada."


    def extract_data(self, html_content):
        """
        Extrae fecha y mensaje de los elementos encontrados.
        Filtra ReTruths y extrae el año.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        valid, msg = self.validate_structure(soup)
        if not valid:
            print(f"❌ ABORTANDO: {msg}")
            return False

        items = soup.find_all("div", {"data-testid": self.SELECTORS["status"]})
        current_batch = []
        
        for item in items:
            # 1. Extraer ID (Nombre de usuario) para filtrar ReTruths
            id_tag = item.find(text=re.compile(r"^@"))
            user_id = id_tag.strip() if id_tag else "@realDonaldTrump"
            
            # FILTRO: Solo posts originales de Trump (No ReTruths)
            if user_id.lower() != "@realdonaldtrump":
                continue

            # 2. Extraer Fecha y Año
            time_tag = item.find("time")
            date_raw = time_tag.get("title") if time_tag else ""
            formatted_time, dt_obj = parse_truth_date(date_raw)
            
            if not dt_obj:
                continue
                
            post_year = dt_obj.year

            # 3. Extraer Texto
            content_div = item.find("div", {"data-testid": self.SELECTORS["content"]})
            message = clean_text(" ".join([p.get_text() for p in content_div.find_all("p")])) if content_div else ""
            
            # 4. Extraer URL del Post
            link_tag = item.find("a", href=re.compile(r"/posts/"))
            post_url = f"https://truthsocial.com{link_tag.get('href')}" if link_tag else None

            current_batch.append({
                "ID": user_id,
                "Time": formatted_time,
                "Year": post_year,
                "Tweet URL": post_url,
                "Tweet Text": message
            })
            
        self.results.extend(current_batch)
        return True


    def save_results(self, filename="raw_truth_data.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"✅ Datos guardados en {filename}")
