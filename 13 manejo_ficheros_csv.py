import pandas as pd
import numpy as np


def guion(): return print('\n--------------------------------------------\n')


#Leer el fichero y retornar un dataframe
movies = pd.read_csv(
    'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv')
print(movies.info())
print(movies.describe())

guion()
gross_earnings = movies['Gross Earnings']
print(gross_earnings.head())
print(gross_earnings.tail())

guion()
#Reemplazar valores nulos
#gross_earnings.fillna(1, inplace=True)
#print(gross_earnings.head())

guion()
#movies['Title'].fillna("N/A", inplace=True)

subDataFrame = movies.loc[:, ['Title', 'Director', 'Gross Earnings',
                              'Facebook Likes - Director', 'Facebook likes - Movie']]
print(subDataFrame.head())

guion()
guion()
subDataFrame['Total likes'] = subDataFrame['Facebook Likes - Director'] + \
    subDataFrame['Facebook likes - Movie']
#print( subDataFrame.head(10) )
#print( subDataFrame.describe() )
pelis_populares = subDataFrame[subDataFrame['Total likes'] > 50000]
print(pelis_populares)

guion()
pelis_x_director = subDataFrame[subDataFrame['Director'] == 'David Fincher']
print(pelis_x_director)

guion()
guion()
tabla = pd.pivot_table(subDataFrame, index=['Director'], aggfunc=[np.sum])
print(tabla)
