import re
from datetime import datetime

def clean_text(text):
    """
    Limpia el texto extraído removiendo espacios extraños
    y caracteres que puedan romper el JSON.
    """
    if not text:
        return ""
    # Remover múltiples espacios y saltos de línea
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def parse_truth_date(date_str):
    """
    Convierte fechas de formato "Apr 06, 2026, 7:13 PM" 
    o similares al formato estándar YYYY-MM-DD HH:MM.
    Retorna (formatted_string, datetime_object)
    """
    if not date_str:
        return None, None
    try:
        # Formato esperado del atributo 'title' en Truth Social
        # Ejemplo: "Apr 06, 2026, 7:13 PM"
        parts = [p.strip() for p in date_str.split(',')]
        if len(parts) >= 3:
            base_date = f"{parts[0]}, {parts[1]}" # "Apr 06, 2026"
            time_st = parts[2] # "7:13 PM"
            full_dt = datetime.strptime(f"{base_date} {time_st}", "%b %d, %Y %I:%M %p")
            return full_dt.strftime("%Y-%m-%d %H:%M"), full_dt
        else:
            # Reintento con formato más simple si falla
            dt = datetime.strptime(date_str.strip(), "%b %d, %Y")
            return dt.strftime("%Y-%m-%d %H:%M"), dt
    except Exception as e:
        print(f"⚠️ Error parseando fecha '{date_str}': {e}")
        return None, None
