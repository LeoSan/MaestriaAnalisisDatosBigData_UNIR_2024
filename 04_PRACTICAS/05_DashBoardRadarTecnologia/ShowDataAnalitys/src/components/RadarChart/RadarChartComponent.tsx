import { useMemo } from 'react';
import {
  Radar, RadarChart, PolarGrid, PolarAngleAxis,
  PolarRadiusAxis, ResponsiveContainer, Tooltip, Legend,
} from 'recharts';
import { ChartProps } from '../../types';
import { CHART_COLORS } from '../../constants';

/**
 * Radar Chart de análisis multidimensional.
 * Compara Health Index, Engagement Rate y Volumen para cada lenguaje.
 * Los valores están normalizados para entrar en la misma escala visual.
 */
export const RadarChartComponent = ({ data }: ChartProps) => {
  const radarData = useMemo(() => {
    const tags = Array.from(new Set(data.map(d => d.tag)));

    const metricsByTag = tags.map(tag => {
      const tagData = data.filter(d => d.tag === tag);
      const count = tagData.length || 1;
      return {
        tag,
        health: tagData.reduce((acc, curr) => acc + curr.health_index, 0) / count,
        engagement: tagData.reduce((acc, curr) => acc + curr.engagement_rate, 0) / count,
        volume: tagData.reduce((acc, curr) => acc + curr.total_questions, 0) / count,
      };
    });

    // Normalizamos para que las tres métricas quepan en el mismo radar
    const formats = [
      { metric: 'Health Index', ...Object.fromEntries(metricsByTag.map(m => [m.tag, m.health])) },
      { metric: 'Engagement (÷10)', ...Object.fromEntries(metricsByTag.map(m => [m.tag, m.engagement / 10])) },
      { metric: 'Volumen (÷1000)', ...Object.fromEntries(metricsByTag.map(m => [m.tag, m.volume / 1000])) },
    ];

    return { formats, tags };
  }, [data]);

  return (
    <div className="bg-white p-4 rounded shadow mb-8">
      <h2 className="text-xl font-bold mb-4 text-center">Análisis Multidimensional (Radar)</h2>
      <div style={{ width: '100%', height: 400 }}>
        <ResponsiveContainer>
          <RadarChart cx="50%" cy="50%" outerRadius="70%" data={radarData.formats}>
            <PolarGrid />
            <PolarAngleAxis dataKey="metric" />
            <PolarRadiusAxis />
            <Tooltip />
            <Legend />
            {radarData.tags.map((tag, i) => (
              <Radar
                key={tag}
                name={tag}
                dataKey={tag}
                stroke={CHART_COLORS[i % CHART_COLORS.length]}
                fill={CHART_COLORS[i % CHART_COLORS.length]}
                fillOpacity={0.5}
              />
            ))}
          </RadarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
