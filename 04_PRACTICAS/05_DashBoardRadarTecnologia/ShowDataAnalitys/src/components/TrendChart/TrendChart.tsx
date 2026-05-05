
import { useMemo, useEffect } from 'react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Legend,
} from 'recharts';
import { ChartProps } from '../../types';
import { CHART_COLORS } from '../../constants';

/**
 * Gráfica de tendencias de volumen.
 * Muestra la media móvil de 3 meses para suavizar la visualización y detectar tracción real.
 */
export const TrendChart = ({ data }: ChartProps) => {
  // 1. Obtener lista única de tags y meses presentes en los datos actuales
  const tags = Array.from(new Set(data.map(d => d.tag)));
  const months = Array.from(new Set(data.map(d => d.year_month))).sort();

  // 2. Pivotar datos para que Recharts pueda graficar múltiples líneas en un solo eje X
  const pivotedData = useMemo(() => {
    if (!data || data.length === 0) return [];
    
    return months.map(month => {
      const entry: any = { year_month: month };
      tags.forEach(tag => {
        const metric = data.find(d => d.tag === tag && d.year_month === month);
        // Fallback a total_questions si rolling_mean_3m no existe (por si hay caché del JSON viejo)
        entry[tag] = metric ? (metric.rolling_mean_3m ?? metric.total_questions) : null;
      });
      return entry;
    });
  }, [data, tags, months]);

  // Log para depuración en el navegador del usuario
  useEffect(() => {
    if (pivotedData.length > 0) {
      console.log('TrendChart pivotedData:', pivotedData[0]);
    }
  }, [pivotedData]);

  if (data.length === 0) {
    return (
        <div className="bg-white p-6 rounded-xl shadow-lg border border-gray-100 mb-8 flex items-center justify-center h-64">
            <p className="text-gray-400 italic">No hay datos suficientes para mostrar tendencias.</p>
        </div>
    );
  }

  return (
    <div className="bg-white p-6 rounded-xl shadow-lg border border-gray-100 mb-8 transition-all hover:shadow-xl">
      <div className="mb-6 text-center">
        <h2 className="text-2xl font-extrabold text-gray-800 tracking-tight">
          Obsolescencia vs Tracción: <span className="text-indigo-600">Tendencias</span>
        </h2>
        <p className="text-gray-500 mt-1 max-w-2xl mx-auto">
          Media móvil de 3 meses del volumen de preguntas. Una pendiente positiva indica adopción, una negativa sugiere madurez o desuso.
        </p>
      </div>

      <div style={{ width: '100%', height: 450 }}>
        <ResponsiveContainer>
          <LineChart data={pivotedData} margin={{ top: 10, right: 30, left: 10, bottom: 20 }}>
            <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
            <XAxis 
              dataKey="year_month" 
              axisLine={false} 
              tickLine={false} 
              tick={{fill: '#64748b', fontSize: 11}}
              dy={15}
              minTickGap={30}
            />
            <YAxis 
              axisLine={false} 
              tickLine={false} 
              tick={{fill: '#64748b', fontSize: 11}}
              tickFormatter={(val) => val >= 1000 ? `${(val / 1000).toFixed(1)}k` : val}
              domain={['auto', 'auto']}
            />
            <Tooltip 
              contentStyle={{ 
                borderRadius: '12px', 
                border: 'none', 
                boxShadow: '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
                padding: '12px'
              }}
              itemStyle={{ fontSize: '13px', fontWeight: 600 }}
              labelStyle={{ fontWeight: 800, marginBottom: '4px', color: '#1e293b' }}
            />
            <Legend 
              verticalAlign="top" 
              align="right"
              iconType="circle"
              wrapperStyle={{ paddingBottom: '25px' }}
            />
            {tags.map((tag, index) => (
              <Line
                key={tag}
                type="monotone"
                dataKey={tag}
                name={tag.toUpperCase()}
                stroke={CHART_COLORS[index % CHART_COLORS.length]}
                strokeWidth={3}
                dot={{ r: 4, strokeWidth: 2, fill: 'white' }}
                activeDot={{ r: 6, strokeWidth: 0 }}
                animationDuration={1000}
                connectNulls
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
