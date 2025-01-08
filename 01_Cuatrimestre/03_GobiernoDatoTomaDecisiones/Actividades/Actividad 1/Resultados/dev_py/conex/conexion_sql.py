import psycopg2
import math
from psycopg2 import DatabaseError

def conectar_sql_server(server, database, username, password):
    try:
        connection = psycopg2.connect(
            host     = server,
            user     = username,
            password = password,
            database = database
        )
        print("Conexión exitosa.")    
        return connection
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
        return 0

def cerrar_sql_server(connection):
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

def consulta_sql_server(SQL_QUERRY, connection, is_return):
    cursor = connection.cursor()
    cursor.execute(SQL_QUERRY)
    if is_return==1:
        rows   = cursor.fetchall()
        return rows     
    else:
        return 0

def insert_data_origen_sql_server(SQL_QUERRY, data, connection):
    cursor = connection.cursor()
    #Validaciones 
    data['FIPS']          = is_empty(data['FIPS'], 0)
    data['Recovered']     = is_empty(data['Recovered'], 0)
    data['Active']        = is_empty(data['Active'], 0)
    #execute 
    cursor.execute(SQL_QUERRY, data)
    connection.commit()

def insert_data_sql_server(SQL_QUERRY, data, connection):
    cursor = connection.cursor()
    #execute 
    cursor.execute(SQL_QUERRY, data)
    connection.commit()

def is_empty(valor, fill):
    if math.isnan(valor) or valor == 'nan' or valor == 'NaN':
        return fill
    else:
        return valor

    