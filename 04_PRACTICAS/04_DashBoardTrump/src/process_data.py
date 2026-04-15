import csv
import json
import os

# Configuración
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Subir un nivel al root
TWEETS_PATH = os.path.join(BASE_DIR, 'data/raw/trump_tweets.csv')
OIL_PATH = os.path.join(BASE_DIR, 'data/raw/brent_oil_prices.csv')
OUTPUT_PATH = os.path.join(BASE_DIR, 'data/processed_data.json')

KEYWORDS = ['oil', 'opec', 'energy', 'saudi', 'iran', 'gas', 'fuel', 'prices', 'production', 'brent', 'shale', 'pipeline']

def process_data():
    print('--- Iniciando Procesamiento de Datos en DashBoardTrump ---')
    print(f'Ruta Tweets: {TWEETS_PATH}')
    print(f'Ruta Oil: {OIL_PATH}')
    
    if not os.path.exists(TWEETS_PATH) or not os.path.exists(OIL_PATH):
        print(f'Error: Faltan archivos en data/raw/')
        return

    # 1. Procesar Precios de Petróleo
    oil_map = {}
    with open(OIL_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['observation_date']
            price = row['DCOILBRENTEU'].strip()
            if price and price != '.':
                try:
                    oil_map[date] = float(price)
                except ValueError:
                    continue

    # 2. Procesar Tweets
    print('Cargando tweets...')
    tweet_map = {}
    with open(TWEETS_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Limpiar llaves de espacios en blanco de forma segura
            clean_row = {}
            for k, v in row.items():
                if k is not None:
                    clean_row[k.strip()] = v
            
            text = (clean_row.get('Tweet Text') or '').lower()
            time_str = (clean_row.get('Time') or '').strip()
            if not time_str: continue
            
            date = time_str.split(' ')[0] # YYYY-MM-DD
            
            # Solo guardamos el primer tweet del día que coincida con palabras clave
            if any(keyword in text for keyword in KEYWORDS):
                if date not in tweet_map:
                    tweet_map[date] = {
                        'text': clean_row.get('Tweet Text'),
                        'url': clean_row.get('Tweet URL')
                    }

    # 3. Preparar Datos para D3: Todo se basa en la serie del petróleo
    final_combined_data = []
    sorted_dates = sorted(oil_map.keys())
    
    for d in sorted_dates:
        # Ampliamos el rango para incluir 2026
        if '2017-01-20' <= d <= '2026-12-31':
            tweet = tweet_map.get(d)
            final_combined_data.append({
                'date': d,
                'price': oil_map[d],
                'tweet_text': tweet['text'] if tweet else "No hay coincidencia",
                'tweet_url': tweet['url'] if tweet else None
            })

    output = {
        'combined_series': final_combined_data
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f'✅ Proceso completado.')
    print(f'- Puntos de tiempo combinados: {len(final_combined_data)}')

if __name__ == '__main__':
    process_data()
