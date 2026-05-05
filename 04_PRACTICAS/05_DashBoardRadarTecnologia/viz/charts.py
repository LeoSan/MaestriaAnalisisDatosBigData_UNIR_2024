import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from core.logger import get_logger

logger = get_logger(__name__)

# Configurar estilo visual
sns.set_theme(style="darkgrid", context="talk")
plt.rcParams['figure.figsize'] = (14, 8)

REPORTS_DIR = Path(__file__).parent.parent / "reports" / "figures"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def plot_rolling_mean(df_metrics: pd.DataFrame):
    """
    Genera un gráfico comparativo de la Media Móvil de 3 meses para el 
    volumen de preguntas de cada tecnología.
    """
    if df_metrics.empty:
        logger.error("El DataFrame está vacío, no se puede graficar.")
        return
        
    logger.info("Generando gráfico de tendencias (Media Móvil de 3 meses)...")
    
    # Ordenar y asegurar que el índice sea de tiempo si es posible, o ordenar al menos
    df = df_metrics.sort_values(by=['tag', 'year_month']).copy()
    
    # Convertir 'year_month' (Period) a timestamp para poder graficar correctamente
    df['date'] = df['year_month'].dt.to_timestamp()
    
    # Calcular media móvil de 3 meses por tecnología
    df['rolling_volume_3m'] = df.groupby('tag')['total_questions'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    
    plt.figure()
    
    # Generar la gráfica usando Seaborn
    ax = sns.lineplot(
        data=df, 
        x='date', 
        y='rolling_volume_3m', 
        hue='tag', 
        marker="o", 
        linewidth=2.5,
        palette="husl"  # Paleta de colores más moderna y vibrante
    )
    
    ax.set_title("Radar de Obsolescencia: Tendencia de Volumen (Media Móvil 3 Meses)", fontsize=18, fontweight='bold')
    ax.set_xlabel("Fecha", fontsize=14)
    ax.set_ylabel("Promedio de Preguntas Mensuales", fontsize=14)
    
    plt.tight_layout()
    
    # Guardar
    out_file = REPORTS_DIR / "volume_rolling_mean.png"
    plt.savefig(out_file, dpi=300)
    plt.close()
    
    logger.info(f"Gráfico guardado exitosamente en: {out_file}")
