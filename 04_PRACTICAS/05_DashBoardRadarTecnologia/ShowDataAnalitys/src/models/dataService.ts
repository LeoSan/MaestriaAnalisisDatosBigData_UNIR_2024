import { TechMetric } from '../types';

/**
 * Obtiene los datos del dashboard desde el JSON estático en /public.
 * Este archivo es generado por el pipeline de Python (processor.py).
 */
export const fetchDashboardData = async (): Promise<TechMetric[]> => {
  const response = await fetch('/data/dashboard_data.json');
  if (!response.ok) {
    throw new Error(`Error al cargar los datos: ${response.statusText}`);
  }
  return await response.json();
};
