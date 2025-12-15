import plotly.graph_objects as go
import plotly.io as pio

class ChartFactory:
    """
    Fábrica de gráficas usando Graph Objects.
    Aquí construimos 'a mano' cada línea (trace) iterando por país,
    lo que nos da control total sobre los datos, igual que en JavaScript.
    """

    def __init__(self):
        # Países que vamos a comparar (nuestros 'datasets' individuales)
        self.focus_countries = ['España', 'Alemania', 'Francia', 'Polonia', 'Suecia', 'Rumania']
        
        # Paleta de colores manual para asegurar distinción (Best Practice)
        self.colors_correct = {
            'España': '#EF4444',   # Rojo
            'Alemania': '#3B82F6', # Azul
            'Francia': '#10B981',  # Verde
            'Polonia': '#F59E0B',  # Amarillo
            'Suecia': '#8B5CF6',   # Violeta
            'Rumania': '#EC4899'   # Rosa
        }

    def create_evolution_chart_correct(self, df):
        """
        Genera la visualización CORRECTA iterando explícitamente.
        Equivalente a tu lógica JS: data = [{x: x1, y: y1}, {x: x2, y: y2}...]
        """
        fig = go.Figure()

        # 1. ITERACIÓN: Generamos los valores múltiples (x, y) para cada país
        for country in self.focus_countries:
            # Filtramos los datos específicos de este país (Tu array xValues / yValues)
            country_data = df[df['Country Name'] == country]
            
            if country_data.empty:
                continue

            # Agregamos la traza (la línea) al gráfico
            fig.add_trace(go.Scatter(
                x=country_data['Year'].tolist(),      # Tus xValues
                y=country_data['Gini'].tolist(),      # Tus yValues
                mode='lines+markers',        # Estilo visual
                name=country,                # Etiqueta de la leyenda
                line=dict(width=2, color=self.colors_correct.get(country, '#999')) # Color asignado
            ))

        # 2. CONFIGURACIÓN DEL LAYOUT (El contenedor)
        fig.update_layout(
            title='Evolución Real de la Desigualdad (2000-2022)',
            xaxis_title='Año',
            yaxis_title='Coeficiente Gini (0-100)',
            template='plotly_white',
            hovermode="x unified", # Muestra todos los valores al pasar el mouse por un año
            yaxis=dict(range=[20, 45]), # Rango Fijo Ético
            legend=dict(title="País")
        )

        return pio.to_json(fig)

    def create_evolution_chart_manipulated(self, df):
        """
        Genera la visualización MANIPULADA.
        Misma lógica de iteración, pero forzando estilos confusos.
        """
        fig = go.Figure()

        # Paleta monocromática confusa (todos tonos de rojo oscuro)
        bad_colors = ['#8B0000', '#9B1010', '#A00000', '#B01010', '#800000', '#900000']

        for i, country in enumerate(self.focus_countries):
            country_data = df[df['Country Name'] == country]
            
            if country_data.empty:
                continue

            fig.add_trace(go.Scatter(
                x=country_data['Year'].tolist(),
                y=country_data['Gini'].tolist(),
                mode='lines', # Sin marcadores para que sea más difícil leer puntos exactos
                name=country,
                # Asignamos colores casi idénticos cíclicamente
                line=dict(width=3, color=bad_colors[i % len(bad_colors)]) 
            ))

        # MANIPULACIÓN: Zoom agresivo en el eje Y
        # Calculamos min y max globales de la muestra seleccionada para truncar
        mask = df['Country Name'].isin(self.focus_countries)
        min_global = df[mask]['Gini'].min()
        max_global = df[mask]['Gini'].max()

        fig.update_layout(
            title='⚠️ CRISIS DE DESIGUALDAD (Escala Manipulada)',
            xaxis_title='Año',
            yaxis_title='Gini',
            template='plotly_dark', # Fondo oscuro para dramatismo
            # El truco sucio: limitar el eje Y exactamente a los datos, sin margen
            yaxis=dict(range=[min_global + 0.1, max_global - 0.1]), 
            showlegend=True 
        )

        return pio.to_json(fig)

# --- PARTE 2.1: SIMILITUD VS DIVERGENCIA ---

    def create_divergence_chart_correct(self, df):
        """
        Ejercicio 1 (Bien): Resaltar similitudes y diferencias[cite: 25].
        Estrategia: Usamos 'Gris' para el contexto y colores fuertes SOLO para los
        países que queremos comparar (ej. Países Nórdicos vs Sur).
        """
        fig = go.Figure()

        # 1. Grupo de Contexto (Gris suave) - Países de fondo
        background_countries = ['Francia', 'Polonia', 'Rumania']
        for country in background_countries:
            country_data = df[df['Country Name'] == country]
            if not country_data.empty:
                fig.add_trace(go.Scatter(
                    x=country_data['Year'], y=country_data['Gini'],
                    mode='lines',
                    name=country,
                    line=dict(width=1, color='#d1d5db'), # Gris claro
                    showlegend=False
                ))

        # 2. Grupo A: Tendencia Estable/Baja (Ej. Suecia - Nórdico)
        suecia = df[df['Country Name'] == 'Suecia']
        if not suecia.empty:
            fig.add_trace(go.Scatter(
                x=suecia['Year'], y=suecia['Gini'],
                mode='lines+markers', name='Suecia (Estable)',
                line=dict(width=3, color='#10B981') # Verde
            ))

        # 3. Grupo B: Tendencia Divergente (Ej. España - Alta/Fluctuante)
        espana = df[df['Country Name'] == 'España']
        if not espana.empty:
            fig.add_trace(go.Scatter(
                x=espana['Year'], y=espana['Gini'],
                mode='lines+markers', name='España (Divergente)',
                line=dict(width=3, color='#EF4444') # Rojo
            ))

        fig.update_layout(
            title='Comparativa Focalizada: Norte vs Sur',
            xaxis_title='Año', yaxis_title='Gini',
            template='plotly_white',
            hovermode="x unified"
        )
        return pio.to_json(fig)

    def create_divergence_chart_bad(self, df):
        """
        Ejercicio 1 (Mal): 'Spaghetti Chart'[cite: 26].
        Superponer demasiadas líneas con colores similares, haciendo imposible leer.
        """
        fig = go.Figure()
        # Tomamos TODOS los países disponibles en el dataframe (son como 30)
        all_countries = df['Country Name'].unique()
        
        for country in all_countries:
            country_data = df[df['Country Name'] == country]
            fig.add_trace(go.Scatter(
                x=country_data['Year'], y=country_data['Gini'],
                mode='lines',
                name=country,
                # Sin grosor destacado, todos compiten por atención
                line=dict(width=1) 
            ))

        fig.update_layout(
            title='Error: Gráfico de Espagueti (Iletrable)',
            template='plotly_white',
            showlegend=False # Ocultamos leyenda porque sería enorme
        )
        return pio.to_json(fig)

    # --- PARTE 2.2: CONTEXTO (SCATTER PLOT) ---

    def create_context_chart_correct(self, df):
        """
        Ejercicio 2 (Bien): Relacionar Gini con Riqueza (PIB)[cite: 29].
        Nota: Como el CSV no tiene PIB, usamos datos aproximados de 2021 para el ejercicio.
        """
        # Datos estáticos de PIB per cápita (2021 aprox en USD) para el contexto
        gdp_data = {
            'Luxemburgo': 133000, 'Irlanda': 100000, 'Suiza': 93000,
            'Noruega': 89000, 'Suecia': 60000, 'Alemania': 51000,
            'Francia': 43000, 'España': 30000, 'Portugal': 24000,
            'Polonia': 18000, 'Rumania': 14000, 'Bulgaria': 11000
        }

        # Filtramos datos del Gini solo para el año 2021
        df_2021 = df[df['Year'] == 2021].copy()
        
        # Cruzamos los datos (Map)
        df_2021['GDP'] = df_2021['Country Name'].map(gdp_data)
        # Eliminamos los que no tengan dato de PIB
        df_context = df_2021.dropna(subset=['GDP'])

        fig = go.Figure()

        # Scatter Plot: Eje X = Riqueza (PIB), Eje Y = Desigualdad (Gini)
        fig.add_trace(go.Scatter(
            x=df_context['GDP'],
            y=df_context['Gini'],
            mode='markers+text',
            text=df_context['Country Name'],
            textposition="top center",
            marker=dict(size=12, color=df_context['Gini'], colorscale='Viridis', showscale=True)
        ))

        fig.update_layout(
            title='Contexto Real: Desigualdad vs. Riqueza (2021)',
            xaxis_title='PIB per Cápita (USD) - Contexto Económico',
            yaxis_title='Coeficiente Gini - Desigualdad',
            template='plotly_white'
        )
        return pio.to_json(fig)

    def create_context_chart_bad(self, df):
        """
        Ejercicio 2 (Mal): Mostrar solo Ranking sin contexto[cite: 30].
        Ignora que un país pobre y uno rico pueden tener el mismo Gini.
        """
        # Filtramos 2021 y ordenamos
        df_2021 = df[df['Year'] == 2021].sort_values(by='Gini')
        # Tomamos top 10 para el bar chart
        df_top = df_2021.head(10)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_top['Country Name'],
            y=df_top['Gini'],
            marker_color='grey'
        ))

        fig.update_layout(
            title='Visión Limitada: Ranking Simple (Sin Contexto Económico)',
            yaxis_title='Gini',
            template='plotly_white'
        )
        return pio.to_json(fig)        