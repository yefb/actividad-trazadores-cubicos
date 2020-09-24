import csv
#modulo donde crearemos la funcion de trazadores cubicos
from tsnip import tcubicos

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
tcubicos(rad_arr)