import datetime

def tcubicos(datos_arr):

    # Declaracion de variables

    x = []  # tiempo
    y = []  # radiacion
    h = []  # delta(x)_i = h_i = x_i - x_i-1
    m = []  # pendiente_i = m_i = (y_i - y_i-1) / (x_i - x_i-1)

    i_arr_xy = 0  # iterador_arr xy

    i_arr_h = 0  # iterador_arr delta de x
    i_arr_x_ant = 0  # iterador_arr x anterior para delta de x

    i_arr_m = 0  # iterador_arr pendiente
    i_arr_y_ant_m = 0  # iterador_arr y anterior para pendiente

    i_arr_tc = 0  # iterador para crear tabla de datos
    row_tabla = {}  # diccionario linea para llenar tabla de datos
    tabla = []  # tabla con lineas de diccionario

    i_arr_sp_x = 1  # iterador para crear splines
    i_arr_sp_x_ant = 1  # iterador para crear splines

    # Final declaracion de variables

    # crear columnas con 'x' y 'y'
    for arr_xy in datos_arr:
        # definimos la columna x
        x.append(arr_xy['time'])

        # definimos la columna y
        y.append(arr_xy['rad'])

        # definimos la columna h

        i_arr_xy = i_arr_xy + 1
        pass

    # crear columna de cambio en el tiempo
    while i_arr_h < len(x):
        date_time_str = x[i_arr_h]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M')

        date_time_str_ant = x[i_arr_x_ant]
        date_time_obj_ant = datetime.datetime.strptime(date_time_str_ant, '%H:%M')

        h.append(date_time_obj - date_time_obj_ant)
        if i_arr_h > 0:
            i_arr_x_ant = i_arr_x_ant + 1
            pass
        i_arr_h = i_arr_h + 1
        pass

    # crear columna de pendiente
    while i_arr_m < len(y):
        # cambio en y
        delta_y = float(y[i_arr_m]) - (float(y[i_arr_y_ant_m]))

        # cambio en x
        delta_x = float(h[1].seconds)
        m.append(delta_y / delta_x)

        if i_arr_m > 0:
            i_arr_y_ant_m = i_arr_y_ant_m + 1
            pass
        i_arr_m = i_arr_m + 1

    # construimos tabla con valores
    while i_arr_tc < len(y):
        row_tabla = {
            'x': x[i_arr_tc],
            'y': y[i_arr_tc],
            'h': (h[i_arr_tc].seconds)/60,
            'm': m[i_arr_tc]
        }

        tabla.append(row_tabla)
        i_arr_tc = i_arr_tc + 1
        pass

    # construimos las ecuaciones
    # tenemos n puntos con n polinomios
    # p_i(x) = cada polinomio con respecto de x, y es de grado 3
    # p_(i) = a_i + b_i(x_i - x_i-1) + c_i(x_i - x_i-1)**2 + d_i(x_i - x_i-1)**3 = y

    while i_arr_sp_x < len(x):        
        
        i__ = str(i_arr_sp_x)
        a = 'a_'+i__+' + '
        b = 'b_'+i__
        c = 'c_'+i__
        d = 'd_'+i__

        expr_ = {
            '0': 'y_'+i__,
            '1': a,
            '2': b+'*'+str(h[i_arr_sp_x].seconds /60)+' + ',
            '3': c+'*'+str(h[i_arr_sp_x].seconds /60 **2)+' + ',
            '4': d+'*'+str(h[i_arr_sp_x].seconds /60 **3)         
        }

        i_arr_sp_x = i_arr_sp_x + 1
        if i_arr_sp_x > 2:
            i_arr_sp_x_ant = i_arr_sp_x_ant + 1
            pass

        
        ts_fn(expr_)

        pass
pass

def ts_fn(expr_):
        print(expr_['0']+' = '+expr_['1']+expr_['2']+expr_['3']+expr_['4'])
        pass