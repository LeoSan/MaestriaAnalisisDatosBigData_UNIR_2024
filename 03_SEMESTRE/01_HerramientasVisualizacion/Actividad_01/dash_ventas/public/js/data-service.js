/**
 * Módulo de Servicio de Datos.
 * Su única responsabilidad es obtener datos de la API del servidor.
 */

export async function fetchData() {
  try {
    //Realizó la petición a la API del servidor definido en el server.js
    const response = await fetch("/api/data");

    if (!response.ok) {
      throw new Error(
        `Error HTTP: ${response.status} - ${response.statusText}`
      );
    }

    //obtengo los datos en formato JSON
    const data = await response.json();
    //console.log("Datos Obtenido Exitosamente:", data);
    return data; 
  } catch (error) {
    console.error("No se pudieron obtener los datos de la API: ❌", error);
    return [];
  }
}
