import time
from core.config import config
from core.logger import get_logger

from extractor.time_utils import generate_monthly_intervals
from extractor.client import StackExtractor
from io_module.storage import save_raw_to_parquet
from analytics.processor import calculate_metrics
from viz.charts import plot_rolling_mean

logger = get_logger("RadarTechPipeline")

def main():
    logger.info("=== Iniciando Pipeline de Radar de Tecnologías ===")
    
    # 1. Extracción y Guardado Raw
    extractor = StackExtractor()
    intervals = generate_monthly_intervals(config.LOOKBACK_MONTHS)
    tags = config.TAGS_LIST
    
    logger.info(f"Se extraerán {config.LOOKBACK_MONTHS} meses para {len(tags)} tags: {tags}")
    
    for tag in tags:
        for idx, (start_unix, end_unix) in enumerate(intervals):
            # Para nombrar el archivo: necesitamos el año-mes del inicio del intervalo
            # Ya sabemos que es el primer día del mes.
            import datetime
            dt = datetime.datetime.fromtimestamp(start_unix)
            year_month = dt.strftime('%Y-%m')
            
            logger.info(f"[{tag}] Extrayendo periodo {year_month}...")
            
            try:
                data = extractor.fetch_data(tag, start_unix, end_unix)
                save_raw_to_parquet(data, tag, year_month)
                
                # Pausa amigable por defecto para no saturar
                time.sleep(1)
            except Exception as e:
                logger.error(f"Fallo en la extracción de {tag} para {year_month}: {str(e)}")
                
    # 2. Transformación y Analytics
    logger.info("Iniciando fase de Analytics...")
    try:
        df_metrics = calculate_metrics()
        
        # Mostrar una muestra en consola
        if not df_metrics.empty:
            logger.info("\nMuestra de las métricas calculadas:")
            print(df_metrics[['tag', 'year_month', 'total_questions', 'engagement_rate', 'health_index']].tail(6))
            
    except Exception as e:
        logger.error(f"Fallo en la fase de Analytics: {str(e)}")
        return
        
    # 3. Visualización
    logger.info("Iniciando fase de Visualización...")
    try:
        plot_rolling_mean(df_metrics)
    except Exception as e:
        logger.error(f"Fallo en la visualización: {str(e)}")
        
    logger.info("=== Pipeline finalizado con éxito ===")

if __name__ == "__main__":
    main()
