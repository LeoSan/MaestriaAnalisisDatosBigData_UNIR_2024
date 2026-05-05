import { useMemo } from 'react';
import { Treemap, ResponsiveContainer, Tooltip } from 'recharts';
import { ChartProps } from '../../types';

/**
 * Treemap de distribución histórica.
 * El área de cada rectángulo es proporcional al volumen total de preguntas de cada lenguaje.
 */
export const TreemapChart = ({ data }: ChartProps) => {
  const treemapData = useMemo(() => {
    const totals: Record<string, number> = {};
    data.forEach(d => {
      totals[d.tag] = (totals[d.tag] || 0) + d.total_questions;
    });
    return Object.entries(totals).map(([name, size]) => ({ name, size }));
  }, [data]);

  return (
    <div className="bg-white p-4 rounded shadow mb-8">
      <h2 className="text-xl font-bold mb-4 text-center">Distribución Histórica (Treemap)</h2>
      <div style={{ width: '100%', height: 300 }}>
        <ResponsiveContainer>
          <Treemap data={treemapData} dataKey="size" stroke="#fff" fill="#6366f1">
            <Tooltip formatter={(value) => [`${value} preguntas`, 'Volumen Total']} />
          </Treemap>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
