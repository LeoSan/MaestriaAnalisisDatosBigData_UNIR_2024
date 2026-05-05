

import {
  ScatterChart, Scatter, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, ZAxis, Legend,
} from 'recharts';
import { ChartProps } from '../../types';
import { CHART_COLORS } from '../../constants';

/**
 * Gráfica de burbujas.
 * Eje X: Tiempo (mes) | Eje Y: Health Index | Tamaño de burbuja: Volumen de preguntas.
 */
export const BubbleChart = ({ data }: ChartProps) => {
  const tags = Array.from(new Set(data.map(d => d.tag)));

  return (
    <div className="bg-white p-4 rounded shadow mb-8">
      <h2 className="text-xl font-bold mb-2 text-center">Burbuja por Tiempo (Salud vs Volumen)</h2>
      <p className="text-sm text-gray-500 mb-4 text-center">
        Eje X: Tiempo | Eje Y: Health Index | Tamaño: Volumen de Preguntas
      </p>
      <div style={{ width: '100%', height: 400 }}>
        <ResponsiveContainer>
          <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
            <CartesianGrid />
            <XAxis type="category" dataKey="year_month" name="Mes" allowDuplicatedCategory={false} />
            <YAxis
              type="number"
              dataKey="health_index"
              name="Health Index"
              domain={[0, 1]}
              tickFormatter={(tick) => `${(tick * 100).toFixed(0)}%`}
            />
            <ZAxis type="number" dataKey="total_questions" range={[50, 800]} name="Volumen" />
            <Tooltip cursor={{ strokeDasharray: '3 3' }} />
            <Legend />
            {tags.map((tag, index) => (
              <Scatter
                key={tag}
                name={tag}
                data={data.filter(d => d.tag === tag)}
                fill={CHART_COLORS[index % CHART_COLORS.length]}
                opacity={0.7}
              />
            ))}
          </ScatterChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
