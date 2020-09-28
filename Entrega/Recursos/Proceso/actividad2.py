from datetime import datetime
import csv
#modulo donde crearemos la funcion de trazadores cubicos
from tsnip import tcubicos
rad_arr = []

#tomando valores del archivo csv
with open('datos.csv') as File:
    reader = csv.reader(File)

# creamos un arreglo con diccionarios con:
    # datatime
    # hora:min
    # correspondiente radicacion
    for row in reader:
        if row[0] == 'time':
            continue

        # Recibe fecha en formato 2020-03-23T10:33:00-05:00 y elimina la primera parte
        fecha_string = row[0].replace('2020-03-23T', '')
        # Recibe el string de la fecha y elimina el token de zona horaria dejando solo la hora
        fecha_string = fecha_string.replace('-05:00', '')
        # transformar el string restante a objeto datetime (con la hora)
        hora_minutos = datetime.strptime(fecha_string, '%H:%M:%S')

        # Procesar registros desde las 06:00 hasta last 17:59
        if 6 <= hora_minutos.hour <= 17:
            rad_arr.append({
                i: row[0],
                'time': fecha_string,
                'rad': row[4]
            })

#pasamos los limites y valores de tiempo y radiacion
tcubicos(rad_arr)




