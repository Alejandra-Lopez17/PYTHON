datos = [
    (2001, 'rosca', 'PT29872', 'Luis Molero', '12/06/2020'),
    (2012, 'piñón', 'EN5698', 'Carlos Rendón',  '12/06/2020'),
    (2010, 'bujía', 'MS9512', 'Pedro Montes', '12/06/2020'),
    (2001, 'bujía', 'JHT222', 'Pedro Faria', '12/06/2020'),
    (2012, 'tijera', 'QW8523', 'Jorge Hernandez', '12/06/2020'),
    (2010, 'bujía', 'ER6523', 'Samir Delgado', '12/06/2020'),
]

'''
Agrupar los vehiculos por el año y anidarlos en el subdiccionario por la placa.
respuesta = {
    2010: {
        'PT29872':{
            'repuesto': 'rosca',
            'fecha_ingreso': '12/06/2020',
            'propietario': 'Luis Molero'
        },
        'EN5698':{
            'repuesto': 'piñón',
            'fecha_ingreso': '12/06/2020',
            'propietario': 'Carlos Rendón'
        }
    }
}
'''
#(2001, 'rosca', 'PT29872', 'Luis Molero', '12/06/2020')


def agrupar_x_modelo(lista_carros: list) -> dict:
    # Crear diccionario vacio
    dict_carros = dict()
    # Iterar lista de carros
    for carro in lista_carros:
        # Desempaquetar tupla
        anio, repuesto, placa, propietario, fecha = carro
        carro = {
            placa: {
                'repuesto': repuesto,
                'fecha_ingreso': fecha,
                'propietario': propietario
            }
        }
        if anio in dict_carros:
            for placa, info in dict_carros[anio].items():
                carro[placa] = info
        dict_carros[anio] = carro
    # retornar diccionario
    return dict_carros


print(agrupar_x_modelo(datos))
