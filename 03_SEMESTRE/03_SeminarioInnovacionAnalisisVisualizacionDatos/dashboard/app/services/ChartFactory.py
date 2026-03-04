import plotly.express as px
import plotly.io as pio
import pandas as pd

class ChartFactory:
    @staticmethod
    def create_sample_chart(df: pd.DataFrame) -> str:
        """
        Genera una gráfica inteligente de Plotly y la exporta a HTML.
        Estilizada para integrarse con un dashboard oscuro de TailwindCSS.
        """
        fig = px.bar(
            df, 
            x='Categoría', 
            y='Ventas', 
            title='Ventas por Categoría',
            color='Categoría', 
            template='plotly_white'
        )
        
        # Ajustes visuales para coincidir con la estética
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#cbd5e1', # Slate-300 de Tailwind
            margin=dict(t=40, b=20, l=20, r=20),
            title_font=dict(size=18, color='#f8fafc'),
            showlegend=False
        )
        
        # Ocultar grid lines
        fig.update_yaxes(showgrid=True, gridcolor='rgba(51, 65, 85, 0.5)')
        fig.update_xaxes(showgrid=False)
        
        return pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
