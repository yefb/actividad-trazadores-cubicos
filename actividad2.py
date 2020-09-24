from datetime import datetime
import csv
#modulo donde crearemos la funcion de trazadores cubicos
from tsnip import tcubicos

# date_time_str = '2020-03-23T10:33:00-05:00'

# date_time_str = date_time_str.replace('2020-03-23T', '')
# date_time_str = date_time_str.replace('-05:00', '')

# date_time_obj = datetime.strptime(date_time_str, '%H:%M:%S')

# print "The hour is", date_time_obj.hour

#valores de limites de tiempo
limit_i = 360
limit_f = 1082

#otras variables
i = 0
rad_arr = []

#tomando valores del archivo csv
with open('datos.csv') as File:
    reader = csv.reader(File)

# creamos un arreglo con diccionarios con:
    # datatime
    # hora:min
    # correspondiente radicacion
    for row in reader:
        if i > limit_i and i < limit_f:
            rad_line = {
                i: row[0],
                'time': row[0][11]+row[0][12]+row[0][13]+row[0][14]+row[0][15],
                'rad': row[4]
            }
            rad_arr.append(rad_line)
            pass

        i = i+1
#pasamos los limites y valores de tiempo y radiacion
print "valores actuales", limit_i, limit_f, rad_arr, "\n"
# tcubicos(limit_i, limit_f, rad_arr)