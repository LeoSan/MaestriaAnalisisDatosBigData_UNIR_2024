import pandas as pd
from pathlib import Path
from io_module.storage import RAW_DIR, PROCESSED_DIR
from core.logger import get_logger

logger = get_logger(__name__)

def calculate_metrics() -> pd.DataFrame:
    """
    Lee todos los archivos Parquet de RAW_DIR, calcula métricas de negocio
    y devuelve un DataFrame unificado y procesado.
    """
    parquet_files = list(RAW_DIR.glob("*.parquet"))
    
    if not parquet_files:
        logger.warning("No hay archivos Parquet para procesar en /data/raw.")
        return pd.DataFrame()
        
    logger.info(f"Procesando {len(parquet_files)} archivos Parquet...")
    
    # Cargar todos los archivos
    dfs = [pd.read_parquet(f) for f in parquet_files]
    df_raw = pd.concat(dfs, ignore_index=True)
    
    # Convertir unix_date a fecha mensual (ej: '2023-01')
    df_raw['date_obj'] = pd.to_datetime(df_raw['unix_date'], unit='s')
    df_raw['year_month'] = df_raw['date_obj'].dt.to_period('M')
    
    # Calcular métricas por tecnología (tag) y mes
    # Para Engagement Rate: sum(score + answers) / sum(views)
    # Para Health Index: mean(answered)
    
    grouped = df_raw.groupby(['tag', 'year_month']).agg(
        total_score=('score', 'sum'),
        total_answers=('answers', 'sum'),
        total_views=('views', 'sum'),
        total_questions=('score', 'count'),
        health_index=('answered', 'mean') # mean de booleanos da el % de True
    ).reset_index()
    
    # Limpiar divisiones por cero en views
    grouped['engagement_rate'] = (grouped['total_score'] + grouped['total_answers']) / grouped['total_views'].replace(0, 1)
    
    # Para el Monthly Trend, ordenamos por tag y mes
    grouped = grouped.sort_values(by=['tag', 'year_month'])
    grouped['monthly_trend_pct'] = grouped.groupby('tag')['total_questions'].pct_change() * 100
    
    # NUEVO: Calcular Media Móvil de 3 meses para el dashboard
    grouped['rolling_mean_3m'] = grouped.groupby('tag')['total_questions'].transform(
        lambda x: x.rolling(window=3, min_periods=1).mean()
    )
    
    # Guardar a Parquet en zona procesada
    out_file = PROCESSED_DIR / "tech_metrics.parquet"
    grouped.to_parquet(out_file, index=False)
    
    # NUEVO: Guardar JSON para React Dashboard (En la carpeta public del frontend)
    json_out_file = Path(__file__).parent.parent / "ShowDataAnalitys" / "public" / "data" / "dashboard_data.json"
    
    # Asegurar que el directorio exista
    json_out_file.parent.mkdir(parents=True, exist_ok=True)
    
    grouped_json = grouped.copy()
    grouped_json['year_month'] = grouped_json['year_month'].astype(str) # Para que JSON lo pueda leer
    grouped_json.to_json(json_out_file, orient='records', force_ascii=False)
    
    # También guardar una copia en data/ por respaldo si se desea, 
    # pero el dashboard lee de public/data/
    backup_json = PROCESSED_DIR.parent / "dashboard_data.json"
    grouped_json.to_json(backup_json, orient='records', force_ascii=False)
    
    logger.info(f"Métricas calculadas y guardadas en {out_file} y {json_out_file}")
    return grouped
