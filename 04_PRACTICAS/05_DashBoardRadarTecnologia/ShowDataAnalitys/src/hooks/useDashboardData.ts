import { useState, useEffect, useMemo } from 'react';
import { TechMetric } from '../types';
import { fetchDashboardData } from '../models/dataService';

/**
 * Controlador principal del dashboard.
 * Orquesta la carga de datos, el estado de filtros y la lógica de negocio.
 */
export const useDashboardData = () => {
  const [data, setData] = useState<TechMetric[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Estado de filtros
  const [selectedTags, setSelectedTags] = useState<string[]>([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const loadData = async () => {
      try {
        const rawData = await fetchDashboardData();
        setData(rawData);
        // Activar todos los tags por defecto al cargar
        const uniqueTags = Array.from(new Set(rawData.map(d => d.tag)));
        setSelectedTags(uniqueTags);
      } catch (err: unknown) {
        setError(err instanceof Error ? err.message : 'Error desconocido');
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  /** Activa o desactiva un lenguaje del filtro global. */
  const toggleTag = (tag: string) => {
    setSelectedTags(prev =>
      prev.includes(tag) ? prev.filter(t => t !== tag) : [...prev, tag]
    );
  };

  /** Datos filtrados por tag seleccionado y término de búsqueda. */
  const filteredData = useMemo(() => {
    let filtered = data.filter(d => selectedTags.includes(d.tag));
    if (searchTerm.trim()) {
      const term = searchTerm.toLowerCase();
      filtered = filtered.filter(
        d => d.year_month.includes(term) || d.tag.toLowerCase().includes(term)
      );
    }
    return filtered;
  }, [data, selectedTags, searchTerm]);

  /** Lista de todos los lenguajes disponibles en el dataset. */
  const allTags = useMemo(
    () => Array.from(new Set(data.map(d => d.tag))),
    [data]
  );

  return {
    data: filteredData,
    rawData: data,
    loading,
    error,
    allTags,
    selectedTags,
    toggleTag,
    searchTerm,
    setSearchTerm,
  };
};
