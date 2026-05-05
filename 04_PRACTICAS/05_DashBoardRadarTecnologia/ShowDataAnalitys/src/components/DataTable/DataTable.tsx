
import { DataTableProps } from '../../types';

/**
 * Tabla de datos crudos con búsqueda en tiempo real.
 * Permite filtrar por lenguaje o por mes (ej. "2024-05").
 */
export const DataTable = ({ data, searchTerm, setSearchTerm }: DataTableProps) => {
  return (
    <div className="bg-white p-4 rounded shadow mb-8 col-span-1 lg:col-span-2">
      <div className="flex flex-col md:flex-row justify-between items-center mb-4">
        <h2 className="text-xl font-bold">Tablero de Datos Crudos</h2>
        <input
          type="text"
          placeholder="Buscar por lenguaje o mes (ej. 2024-05)..."
          className="border p-2 rounded w-full md:w-72 mt-2 md:mt-0 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
        />
      </div>
      <div className="overflow-x-auto h-96 border rounded">
        <table className="min-w-full table-auto text-sm text-left">
          <thead className="bg-gray-100 sticky top-0 shadow-sm">
            <tr>
              <th className="px-4 py-3 border-b font-semibold">Mes</th>
              <th className="px-4 py-3 border-b font-semibold">Lenguaje</th>
              <th className="px-4 py-3 border-b font-semibold">Volumen (Qs)</th>
              <th className="px-4 py-3 border-b font-semibold">Score Total</th>
              <th className="px-4 py-3 border-b font-semibold">Health Index</th>
              <th className="px-4 py-3 border-b font-semibold">Engagement</th>
            </tr>
          </thead>
          <tbody>
            {data.length === 0 ? (
              <tr>
                <td colSpan={6} className="text-center py-8 text-gray-400 italic">
                  No hay datos que coincidan con la búsqueda.
                </td>
              </tr>
            ) : (
              data.map((row, i) => (
                <tr key={`${row.tag}-${row.year_month}-${i}`} className="hover:bg-indigo-50 transition-colors">
                  <td className="px-4 py-2 border-b text-gray-700">{row.year_month}</td>
                  <td className="px-4 py-2 border-b font-semibold capitalize text-indigo-600">{row.tag}</td>
                  <td className="px-4 py-2 border-b">{row.total_questions.toLocaleString()}</td>
                  <td className="px-4 py-2 border-b">{row.total_score.toLocaleString()}</td>
                  <td className="px-4 py-2 border-b">{(row.health_index * 100).toFixed(1)}%</td>
                  <td className="px-4 py-2 border-b">{row.engagement_rate.toFixed(2)}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};
