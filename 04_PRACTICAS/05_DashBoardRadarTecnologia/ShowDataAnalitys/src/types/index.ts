/**
 * Representa una fila de métricas calculadas por el pipeline de Python.
 * Corresponde a una tecnología (tag) en un mes específico.
 */
export interface TechMetric {
  tag: string;
  year_month: string;
  total_score: number;
  total_answers: number;
  total_views: number;
  total_questions: number;
  health_index: number;
  engagement_rate: number;
  monthly_trend_pct: number | null;
  rolling_mean_3m: number;
}

/**
 * Props base que reciben todos los componentes de gráficas.
 */
export interface ChartProps {
  data: TechMetric[];
}

/**
 * Props específicas del componente DataTable.
 */
export interface DataTableProps extends ChartProps {
  searchTerm: string;
  setSearchTerm: (s: string) => void;
}
