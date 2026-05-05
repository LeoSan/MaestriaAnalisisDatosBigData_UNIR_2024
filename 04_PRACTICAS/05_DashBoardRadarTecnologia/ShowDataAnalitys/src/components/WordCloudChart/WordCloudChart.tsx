import { useMemo } from 'react';
import ReactWordcloud from 'react-wordcloud';
import { ChartProps } from '../../types';
import { WORDCLOUD_OPTIONS } from '../../constants';

// Solución para compatibilidad CJS/ESM con Vite
const WordCloud = (ReactWordcloud as any).default || ReactWordcloud;

/**
 * Nube de palabras.
 * El tamaño de cada lenguaje es proporcional al volumen total de preguntas históricas.
 */
export const WordCloudChart = ({ data }: ChartProps) => {
  const words = useMemo(() => {
    const totals: Record<string, number> = {};
    data.forEach(d => {
      totals[d.tag] = (totals[d.tag] || 0) + d.total_questions;
    });
    return Object.entries(totals).map(([text, value]) => ({ text, value }));
  }, [data]);

  return (
    <div className="bg-white p-4 rounded shadow mb-8">
      <h2 className="text-xl font-bold mb-4 text-center">Nube de Tecnologías (Por Volumen)</h2>
      <div style={{ width: '100%', height: 300 }}>
        <WordCloud words={words} options={WORDCLOUD_OPTIONS} />
      </div>
    </div>
  );
};
