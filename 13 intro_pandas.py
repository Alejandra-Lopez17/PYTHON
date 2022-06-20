import pandas as pd


def guion(): return print('--------------------------------------------')


#Crear serie
serie = pd.Series([100, 80, 150, 200], index=[
                  'Enero', 'Febrero', 'Marzo', 'Abril'])
print(serie)

guion()
#Acceder al objeto que contiene el indice
print(serie.index)
guion()
serie.index = ['ene', 'feb', 'mar', 'abr']
print(serie)

#Obtener el tipo de dato de la serie
guion()
print(serie.dtype)

guion()
print(serie.shape)
print(serie.axes)

#Acceder a un valor de la serie
guion()
print(serie[0])
print(serie['ene'])

guion()
serie.index.name = 'Meses'
serie.name = 'Ventas 2021'

print(serie)

guion()
print('DATAFRAME')
guion()

dict_ventas = {
    'frutas': [100, 200, 400, 160, 200, 600, 300, 200, 100, 840, 320, 160],
    'aseo': [200, 150, 110, 180, 320, 560, 510, 890, 650, 120, 520, 900]
}
#Crear dataframe
ventas = pd.DataFrame(dict_ventas, index=[
                      'ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
print(ventas)

guion()
#Identificadores de las columnas
print(ventas.columns)

guion()
print(ventas.index)

guion()
#Obtener las dimensiones del dataframe
print(ventas.axes)
guion()
print(ventas.shape)

#Agregar etiquetas a los indices
ventas.index.name = 'Meses'
ventas.columns.name = 'Productos'
print(ventas)

guion()
total_x_mes = ventas['frutas'] + ventas.aseo
print(total_x_mes)
guion()
ventas['total ventas'] = total_x_mes
print(ventas)

guion()
utilidades = 0.2
respuesta = ventas['total ventas'] * utilidades
ventas['utilidades'] = respuesta
print(ventas)

guion()
ganancias = ventas.utilidades
total = sum(ganancias)
print('Ganancias totales: ', total)

guion()
#Obtener los primeros 5 registros del dataframe
print(ventas.head())
guion()
print(ventas.head(8))

guion()
#Obtener los últimos 5 registros
print(ventas.tail())

guion()
#Obtener registro de manera aleatoria
registro = ventas.sample()
print(registro)

guion()
print(ventas.sample(2))

guion()
info = ventas.info()
print(info)

guion()
print(ventas.describe())

guion()
print('SELECCIÓN DE DATOS')
guion()
seleccion = ventas['total ventas'] > 900
print(seleccion)
ejemplo_seleccion = ventas[seleccion]
print(ejemplo_seleccion)

guion()
serie = pd.Series([100, 80, 150, 200], index=[
                  'Enero', 'Febrero', 'Marzo', 'Abril'])
seleccion = serie[[True, False, True, False]]
print(seleccion)

guion()
seleccion = serie > 100
print(seleccion)

guion()
diccionario = {'ventas': serie}
dataframe = pd.DataFrame(diccionario)
print(dataframe)
