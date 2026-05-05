/**
 * Paleta de colores compartida por todas las gráficas del dashboard.
 * Centralizar los colores aquí garantiza consistencia visual.
 */
export const CHART_COLORS: string[] = [
  '#6366f1', // indigo
  '#22c55e', // green
  '#f59e0b', // amber
  '#ef4444', // red
  '#06b6d4', // cyan
  '#a855f7', // purple
  '#f97316', // orange
];

/**
 * Configuración de la fuente y estilos base para react-wordcloud.
 */
export const WORDCLOUD_OPTIONS = {
  rotations: 2,
  rotationAngles: [-90, 0] as [number, number],
  fontSizes: [30, 90] as [number, number],
  fontFamily: 'Inter, sans-serif',
};
