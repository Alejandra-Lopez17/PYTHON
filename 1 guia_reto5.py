import pandas as pd

def listaPeliculas(rutaFileCsv: str)->str:
    if ".csv" in rutaFileCsv:
        try:
            lectura = pd.read_csv(rutaFileCsv)
            subtabla = lectura[["Country","Language","Gross Earnings"]]
            nueva = pd.pivot_table(subtabla,index=["Country","Language"],values='Gross Earnings')
            return nueva.head(10)
        except:
            return "Error al leer el archivo de datos."
    else:
        return "Extensión inválida"

rutaFileCsv='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'
print(listaPeliculas(rutaFileCsv))