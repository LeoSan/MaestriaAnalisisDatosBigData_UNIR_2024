import { useDashboardData } from './hooks/useDashboardData';
import { BubbleChart } from './components/BubbleChart';
import { TrendChart } from './components/TrendChart';
import { TreemapChart } from './components/TreemapChart';
import { RadarChartComponent } from './components/RadarChart';
import { WordCloudChart } from './components/WordCloudChart';
import { DataTable } from './components/DataTable';

function App() {
  const {
    data,
    loading,
    error,
    allTags,
    selectedTags,
    toggleTag,
    searchTerm,
    setSearchTerm,
  } = useDashboardData();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-xl font-semibold animate-pulse text-indigo-600">
          Cargando métricas…
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 text-red-500 font-bold">
        Error: {error}
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-4 md:p-8">
      {/* Encabezado */}
      <header className="mb-8 text-center md:text-left">
        <h1 className="text-3xl md:text-4xl font-extrabold text-gray-800 tracking-tight">
          Radar de Tecnologías <span className="text-indigo-600">Pro</span>
        </h1>
        <p className="text-gray-500 mt-2">
          Visualización interactiva de métricas extraídas de Stack Exchange · Arquitectura MVC + Static Data App
        </p>
      </header>

      {/* Filtro Global */}
      <section aria-label="Filtro por lenguaje" className="bg-white p-4 rounded shadow mb-8">
        <h2 className="font-bold mb-3 text-gray-700">Filtrar por Lenguaje:</h2>
        <div className="flex flex-wrap gap-2">
          {allTags.map(tag => (
            <button
              key={tag}
              onClick={() => toggleTag(tag)}
              className={`px-4 py-2 rounded-full text-sm font-semibold transition-colors ${selectedTags.includes(tag)
                  ? 'bg-indigo-600 text-white shadow-md'
                  : 'bg-gray-200 text-gray-600 hover:bg-gray-300'
                }`}
            >
              {tag}
            </button>
          ))}
        </div>
      </section>

      {/* Grid de Gráficas */}
      <main className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="col-span-1 lg:col-span-2">
          <TrendChart data={data} />
        </div>

        <div className="col-span-1 lg:col-span-2">
          <BubbleChart data={data} />
        </div>

        <div className="col-span-1">
          <TreemapChart data={data} />
        </div>

        <div className="col-span-1">
          <WordCloudChart data={data} />
        </div>

        <div className="col-span-1 lg:col-span-2">
          <RadarChartComponent data={data} />
        </div>

        <DataTable data={data} searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      </main>

      <footer className="mt-12 text-center text-gray-400 text-sm">
        <p>Soluciones a base de curiosidades, parte de un proyecto personal Tech  (Python + Parquet)</p>
      </footer>
    </div>
  );
}

export default App;
