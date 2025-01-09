import pandas as pd
from conex import conexion_sql

# Reemplaza 'tu_archivo.csv' por el nombre real de tu archivo
df = pd.read_csv('/Users/leonard/Documents/MaestriaAnalisisDatosBigData_UNIR_2024/01_Cuatrimestre/03_GobiernoDatoTomaDecisiones/Actividades/Actividad 1/Resultados/dev_py/03032023.csv')

connection = conexion_sql.conectar_sql_server(
    server   ='localhost',
    database ='practica_dataset',
    username ='leonard',
    password ='admin'
)

#Limpio base de datos
conexion_sql.consulta_sql_server('DELETE FROM t_origen_dataset', connection, 0)

# Inicio la extracion de data
print("Extracción Inicianda.")
total_datos = 0
for index, row in df.iterrows():
    #print(row)
    SQL_QUERRY = "INSERT INTO t_origen_dataset (fips, admin2, province_state, country_region, last_update, lat, long, confirmed, deaths, recovered, active, combined_key, incident_rate, case_fatality_ratio) VALUES (%(FIPS)s, %(Admin2)s, %(Province_State)s, %(Country_Region)s, %(Last_Update)s, %(Lat)s, %(Long_)s, %(Confirmed)s, %(Deaths)s, %(Recovered)s, %(Active)s, %(Combined_Key)s, %(Incident_Rate)s, %(Case_Fatality_Ratio)s)"
    conexion_sql.insert_data_origen_sql_server(SQL_QUERRY, row, connection)
    total_datos=total_datos + 1

print("Extracción Finalizada")
print("")
print("Un total de {} datos extraidos exitosamente del dataset.".format(total_datos))

## Transformacion 
lista_province_state = conexion_sql.consulta_sql_server('SELECT province_state FROM t_origen_dataset GROUP BY province_state ORDER BY province_state', connection, 1)
lista_country_region = conexion_sql.consulta_sql_server('SELECT country_region FROM t_origen_dataset GROUP BY country_region ORDER BY country_region', connection, 1)

#Limpio base de datos
conexion_sql.consulta_sql_server('DELETE FROM t_dim_region', connection, 0)
conexion_sql.consulta_sql_server('DELETE FROM t_dim_pais', connection, 0)

for province_state in lista_province_state: # type: ignore
    datos_a_insertar = {'nombre': province_state[0] }
    SQL_QUERRY = "INSERT INTO t_dim_region (nombre) VALUES (%(nombre)s)"
    conexion_sql.insert_data_sql_server(SQL_QUERRY, datos_a_insertar, connection)


for country_region in lista_country_region: # type: ignore
    datos_a_insertar = {'nombre': country_region[0] }
    SQL_QUERRY = "INSERT INTO t_dim_pais (nombre) VALUES (%(nombre)s)"
    conexion_sql.insert_data_sql_server(SQL_QUERRY, datos_a_insertar, connection)

#Inserto los datos a la tabla t_hechos 
lista_t_hechos = conexion_sql.consulta_sql_server('SELECT fips, last_update, confirmed, deaths, recovered, active, incident_rate, case_fatality_ratio, b.id, c.id FROM t_origen_dataset  as a LEFT JOIN t_dim_pais as b ON b.nombre = a.country_region LEFT JOIN t_dim_region as c ON c.nombre = a.province_state', connection, 1)

total_datos = 0

for t_hechos in lista_t_hechos: # type: ignore
    datos_a_insertar = {'fips': t_hechos[0], 'fecha':t_hechos[1], 'confirmed':t_hechos[2],'deaths':t_hechos[3], 'recovered':t_hechos[4], 'active':t_hechos[5], 'incident_rate': conexion_sql.is_empty(t_hechos[6], 0), 'case_fatality_ratio':conexion_sql.is_empty(t_hechos[7], 0), 'fk_pais':t_hechos[8], 'fk_region':t_hechos[9]}
    print("")
    print(" --- data N°{} ".format(total_datos))
    print(datos_a_insertar)
    print("")
    total_datos=total_datos + 1
    SQL_QUERRY = "INSERT INTO t_hechos (fips, fecha, confirmed, deaths, recovered, active, incident_rate, case_fatality_ratio, fk_pais, fk_region) VALUES (%(fips)s, %(fecha)s, %(confirmed)s, %(deaths)s, %(recovered)s, %(active)s, %(incident_rate)s, %(case_fatality_ratio)s, %(fk_pais)s, %(fk_region)s)"
    conexion_sql.insert_data_sql_server(SQL_QUERRY, datos_a_insertar, connection)

conexion_sql.cerrar_sql_server(connection)
