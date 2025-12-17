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

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
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

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
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

    def create_divergence_chart_correct(self, df):
        """
        Ejercicio 1 (Bien): Resaltar similitudes y diferencias[cite: 25].
        Estrategia: Usamos 'Gris' para el contexto y colores fuertes SOLO para los
        países que queremos comparar (ej. Países Nórdicos vs Sur).

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        fig = go.Figure()

        # 1. Grupo de Contexto (Gris suave) - Países de fondo
        background_countries = ['Francia', 'Polonia', 'Rumania']
        for country in background_countries:
            country_data = df[df['Country Name'] == country]
            if not country_data.empty:
                fig.add_trace(go.Scatter(
                    x=country_data['Year'].tolist(), 
                    y=country_data['Gini'].tolist(),
                    mode='lines',
                    name=country,
                    line=dict(width=1, color='#d1d5db'), # Gris claro
                    showlegend=False
                ))

        # 2. Grupo A: Tendencia Estable/Baja (Ej. Suecia - Nórdico)
        suecia = df[df['Country Name'] == 'Suecia']
        if not suecia.empty:
            fig.add_trace(go.Scatter(
                x=suecia['Year'].tolist(), 
                y=suecia['Gini'].tolist(),
                mode='lines+markers', name='Suecia (Estable)',
                line=dict(width=3, color='#10B981') # Verde
            ))

        # 3. Grupo B: Tendencia Divergente (Ej. España - Alta/Fluctuante)
        espana = df[df['Country Name'] == 'España']
        if not espana.empty:
            fig.add_trace(go.Scatter(
                x=espana['Year'].tolist(), 
                y=espana['Gini'].tolist(),
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

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        fig = go.Figure()
        # Tomamos TODOS los países disponibles en el dataframe (son como 30)
        all_countries = df['Country Name'].unique()
        
        for country in all_countries:
            country_data = df[df['Country Name'] == country]
            fig.add_trace(go.Scatter(
                x=country_data['Year'].tolist(), 
                y=country_data['Gini'].tolist(),
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

    def create_context_chart_correct(self, df):
        """
        Ejercicio 2 (Bien): Relacionar Gini con Riqueza (PIB)[cite: 29].
        Nota: Como el CSV no tiene PIB, usamos datos aproximados de 2021 para el ejercicio.

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
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
            x=df_context['GDP'].tolist(),
            y=df_context['Gini'].tolist(),
            mode='markers+text',
            text=df_context['Country Name'].tolist(),
            textposition="top center",
            marker=dict(size=12, color=df_context['Gini'].tolist(), colorscale='Viridis', showscale=True)
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

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        # Filtramos 2021 y ordenamos
        df_2021 = df[df['Year'] == 2021].sort_values(by='Gini')
        # Tomamos top 10 para el bar chart
        df_top = df_2021.head(10)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_top['Country Name'].tolist(),
            y=df_top['Gini'].tolist(),
            marker_color='grey'
        ))

        fig.update_layout(
            title='Visión Limitada: Ranking Simple (Sin Contexto Económico)',
            yaxis_title='Gini',
            template='plotly_white'
        )
        return pio.to_json(fig)        

    # --- PARTE 3.1: POLÍTICAS PÚBLICAS (PROYECCIÓN) ---
    def create_policy_chart_correct(self, df):
        """
        Ejercicio 3 (Correcto): Proyección Ética.
        Muestra la historia completa para dar contexto y diferencia claramente
        lo real de lo hipotético usando líneas punteadas.

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        fig = go.Figure()

        # 1. DATOS REALES (Historia)
        # Filtramos España y aseguramos orden por año
        esp_real = df[df['Country Name'] == 'España'].sort_values(by='Year')
        
        if esp_real.empty:
            return pio.to_json(fig) # Retorno vacío seguro

        # Agregamos la traza histórica (Línea sólida azul)
        fig.add_trace(go.Scatter(
            x=esp_real['Year'].tolist(), 
            y=esp_real['Gini'].tolist(),
            mode='lines+markers', 
            name='Histórico Real',
            line=dict(color='#3B82F6', width=3) # Azul estándar
        ))

        # 2. DATOS HIPOTÉTICOS (La Proyección de tu Política)
        # Tomamos el último dato real como punto de partida para que empalme bien
        last_year = int(esp_real['Year'].max())
        last_val = float(esp_real['Gini'].iloc[-1])

        # Creamos los arrays manuales de la proyección (2022-2026)
        # Simulamos una bajada optimista por la "política pública"
        proj_x = [last_year, last_year + 1, last_year + 2, last_year + 3, last_year + 4]
        proj_y = [last_val,   last_val - 0.5, last_val - 1.1, last_val - 1.5, last_val - 1.8]

        # Agregamos la traza proyectada (Línea punteada verde)
        fig.add_trace(go.Scatter(
            x=proj_x, 
            y=proj_y,
            mode='lines+markers', 
            name='Proyección (Reforma Fiscal)',
            line=dict(color='#10B981', width=3, dash='dot') # <--- CLAVE: dash='dot' indica estimación
        ))

        # 3. LAYOUT ÉTICO
        fig.update_layout(
            title='Proyección de Impacto: Reforma Fiscal (Contexto Completo)',
            xaxis_title='Año', 
            yaxis_title='Índice Gini',
            template='plotly_white',
            hovermode="x unified",
            # Escala Y amplia (0-45 o similar) para mostrar la magnitud real del cambio
            yaxis=dict(range=[25, 40]) 
        )
        return pio.to_json(fig)

    def create_policy_chart_bad(self, df):
        """
        Ejercicio 3 (Manipulado): Exageración de Efectos.
        Ocultamos la historia y truncamos el eje para que una bajada pequeña parezca gigante.

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        fig = go.Figure()

        # Usamos SOLO los datos de la proyección (ignorando la historia previa)
        # Hardcodeamos los mismos datos de la proyección anterior
        # Suponemos que el último real fue aprox 33.0
        proj_x = [2022, 2023, 2024, 2025, 2026]
        proj_y = [33.0, 32.5, 31.9, 31.5, 31.2]

        # Traza manipulada visualmente
        fig.add_trace(go.Scatter(
            x=proj_x, 
            y=proj_y,
            mode='lines+markers', 
            name='Impacto Política',
            line=dict(color='#EF4444', width=5), # Línea muy gruesa y roja
            fill='tozeroy' # Relleno bajo la curva para dar sensación de volumen/masa
        ))

        # CÁLCULO DE LA MANIPULACIÓN
        min_val = min(proj_y)
        max_val = max(proj_y)

        # LAYOUT MANIPULADO
        fig.update_layout(
            title='¡REDUCCIÓN DRÁSTICA DE LA DESIGUALDAD!',
            xaxis_title='Año Proyectado', 
            yaxis_title='Gini',
            template='plotly_white',
            # TRUCO SUCIO: Eje Y cortado milimétricamente al rango de datos
            # De 33.0 a 31.2, el rango es solo 1.8 puntos, pero ocupará todo el alto del div
            yaxis=dict(range=[min_val - 0.1, max_val + 0.1]) 
        )
        return pio.to_json(fig)     

    # --- EJERCICIO 4: ANÁLISIS DE CRISIS (COVID-19) ---
    def create_crisis_chart_correct(self, df):
        """
        Ejercicio 4 (Correcto): Análisis con Contexto Histórico.
        Mostramos la década completa (2010-2022) para evaluar si el repunte
        del COVID-19 fue realmente una anomalía grave o una fluctuación estándar.

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        # Seleccionamos un país con datos claros (Alemania)
        target_country = 'Alemania'
        
        # Filtramos la última década completa
        df_context = df[
            (df['Country Name'] == target_country) & 
            (df['Year'] >= 2010)
        ].sort_values(by='Year')

        if df_context.empty:
            return pio.to_json(go.Figure())

        fig = go.Figure()

        # Línea de tendencia histórica
        fig.add_trace(go.Scatter(
            x=df_context['Year'].tolist(), 
            y=df_context['Gini'].tolist(),
            mode='lines+markers', 
            name=target_country,
            line=dict(color='#6366F1', width=3) # Color Índigo profesional
        ))

        # ANOTACIÓN CLAVE: Marcamos el inicio de la crisis
        # Esto cumple con "relacionar tendencias con la crisis"
        fig.add_annotation(
            x=2020, 
            y=df_context[df_context['Year'] == 2020]['Gini'].values[0],
            text="Crisis COVID-19",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#EF4444"
        )

        fig.update_layout(
            title=f'Impacto Real del COVID-19: {target_country} (2010-2022)',
            xaxis_title='Año', 
            yaxis_title='Índice Gini',
            template='plotly_white',
            hovermode="x unified",
            # Escala honesta que permite ver las fluctuaciones previas
            yaxis=dict(range=[28, 34]) 
        )
        return pio.to_json(fig)

    def create_crisis_chart_bad(self, df):
        """
        Ejercicio 4 (Manipulado): 'Cherry Picking' (Falta de Contexto).
        Aislamos solo el año previo y el año de la crisis.
        Al borrar la historia, cualquier subida parece un desastre sin precedentes.

        Args:
            df (pd.DataFrame): Dataframe con columnas 'Country Name', 'Year', 'Gini'.

        Returns:
            str: JSON string de la figura Plotly.
        """
        target_country = 'Alemania'
        
        # TRAMPA: Seleccionamos SOLO 2 años
        df_cherry = df[
            (df['Country Name'] == target_country) & 
            (df['Year'].isin([2019, 2020]))
        ].sort_values(by='Year')

        fig = go.Figure()

        # Usamos BARRAS para que la diferencia de altura se sienta más "pesada"
        fig.add_trace(go.Bar(
            x=df_cherry['Year'].tolist(), 
            y=df_cherry['Gini'].tolist(),
            name=target_country,
            # Color gris para 2019, Rojo Alarma para 2020
            marker_color=['#9CA3AF', '#EF4444'],
            text=df_cherry['Gini'].tolist(), # Mostramos el valor para que vean que subió
            textposition='auto'
        ))

        fig.update_layout(
            title='¡IMPACTO DEVASTADOR DEL COVID-19!',
            xaxis=dict(
                tickmode='array', 
                tickvals=[2019, 2020],
                title='Año (Sin contexto previo)'
            ),
            yaxis_title='Gini',
            template='plotly_white',
            # MANIPULACIÓN: Truncamos el eje Y para exagerar la diferencia visual
            # De 31.8 a 32.4 hay solo 0.6 puntos, pero aquí parecerá el doble.
            yaxis=dict(range=[31.0, 33.0]) 
        )
        return pio.to_json(fig)           