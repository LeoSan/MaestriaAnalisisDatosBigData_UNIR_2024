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

conexion_sql.cerrar_sql_server(connection)
