import csv
import pandas as pd

note = ''

with open('/Users/leonard/Documents/MaestriaAnalisisDatosBigData_UNIR_2024/01_Cuatrimestre/03_GobiernoDatoTomaDecisiones/Actividades/Actividad 1/Resultados/dev_py/03032023.csv', newline='') as f:
    data  = csv.reader(f, delimiter=',')
    notes = list(data)

def getData(notes): 
    data = []
    for i in range(1, len(notes)):
        list_limpia = []
        for j in range(len(notes[i])):
            #print(notes[0][j] + '  '+ notes[i][j] )
            if j < len(list_limpia):
                list_limpia[j] = notes[i][j]
            else:
                # Si j está fuera de rango, puedes agregar el elemento al final
                list_limpia.append(notes[i][j])
        #print(list_limpia)
        data.append(list_limpia)
    
    print(data)
    print('')

getData(notes)